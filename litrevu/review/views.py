from itertools import chain
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Value, CharField, Q
from . import forms, models


@login_required
def feed(request):
    follows = [follow.followed_user for follow in models.UserFollow.objects.filter(user=request.user)]
    tickets = models.Ticket.objects.filter(Q(user__in=follows) | Q(user=request.user))
    reviews = models.Review.objects.filter(Q(user__in=follows) | Q(user=request.user) | Q(ticket__user=request.user))
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
    already_reviewed = [review.ticket for review in reviews if review.user == request.user]
    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)
    return render(request, "review/feed.html", {"posts": posts, "already_reviewed": already_reviewed})


@login_required
def posts(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
    posts = sorted(chain(tickets, reviews), key=lambda post: post.time_created, reverse=True)
    return render(request, "review/posts.html", {"posts": posts})


@login_required
def follows(request):
    follows = models.UserFollow.objects.filter(user=request.user)
    followers = models.UserFollow.objects.filter(followed_user=request.user)
    error_message = ""
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        try:
            user = get_user_model().objects.get(username=user_name)
        except get_user_model().DoesNotExist:
            user = None
            error_message = f"{user_name} ne correspond à aucun utilisateur !"
        already_followed = [follow.followed_user for follow in models.UserFollow.objects.filter(user=request.user)]
        if user and user != request.user and user not in already_followed:
            models.UserFollow.objects.create(user=request.user, followed_user=user)
    return render(
        request,
        "review/follows.html",
        {
            "follows": follows,
            "followers": followers,
            "error_message": error_message
        }
    )


@login_required
def delete_follow(request, follow_id):
    follow = models.UserFollow.objects.get(id=follow_id)
    follow.delete()
    return redirect("follows")


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("feed")
    return render(request, "review/create_ticket.html", {'ticket_form': form})


@login_required
def update_ticket(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    if ticket.user != request.user:
        return redirect('feed')
    form = forms.TicketForm(instance=ticket)
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('posts')
    return render(request, "review/update_ticket.html", {'ticket_form': form, 'ticket': ticket})


@login_required
def delete_ticket(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    if ticket.user != request.user:
        return redirect('feed')
    if request.method == "POST":
        ticket.delete()
        return redirect("posts")
    return render(request, "review/delete_ticket.html", {"ticket": ticket})


@login_required
def create_review_and_ticket(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('feed')
    return render(
        request,
        "review/create_review_and_ticket.html",
        {
            'ticket_form': ticket_form,
            "review_form": review_form
        }
    )


@login_required
def create_review(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    form = forms.ReviewForm()
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('feed')
    return render(request, "review/create_review.html", {'review_form': form, 'ticket': ticket})


@login_required
def update_review(request, review_id):
    review = models.Review.objects.get(id=review_id)
    if review.user != request.user:
        return redirect("feed")
    form = forms.ReviewForm(instance=review)
    if request.method == "POST":
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("posts")
    return render(request, "review/update_review.html", {'review_form': form, 'ticket': review.ticket})


@login_required
def delete_review(request, review_id):
    review = models.Review.objects.get(id=review_id)
    if review.user != request.user:
        return redirect('feed')
    if request.method == "POST":
        review.delete()
        return redirect("posts")
    return render(request, "review/delete_review.html", {"review": review})
