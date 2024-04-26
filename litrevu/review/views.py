from itertools import chain
from django.db.models import CharField, Value
from django.shortcuts import render, redirect
from .forms import TicketForm, ReviewForm
from .models import Ticket, Review, UserFollows
from authentication.models import User

def feed_view(request):
    tickets = Ticket.objects.all()
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.all()
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    return render(request, 'review/feed.html', {'posts': posts})

def create_ticket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('feed')
    return render(request, "review/create_ticket.html", {'form': form})

def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    form = TicketForm(instance=ticket)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('feed')
    return render(request, 'review/update_ticket.html', {'form': form})

def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('feed')
    return render(request, 'review/delete_ticket.html', {'ticket': ticket})

def create_review(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('feed')
    return render(request, "review/create_review.html", {'form': form})

def update_review(request, review_id):
    review = Review.objects.get(id=review_id)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('feed')
    return render(request, 'review/update_review.html', {'form': form})

def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('feed')
    return render(request, 'review/delete_review.html', {'review': review})

def follows_view(request):
    user_follows = UserFollows.objects.filter(user=request.user)
    user_followers = UserFollows.objects.filter(followed_user=request.user)
    if request.method == 'POST':
        if request.POST.get("delete"):
            print(request.POST)
            user = User.objects.get(id=request.POST.get("delete"))
            UserFollows.objects.get(user=request.user, followed_user=user).delete()
        else:
            user_name = request.POST.get("user_name")
            try:
                user = User.objects.get(username=user_name)
            except User.DoesNotExist:
                user = None
            if user and user.id != request.user.id:
                UserFollows.objects.create(user=request.user, followed_user=user)
        return redirect('follows')
    return render(request, "review/follows_view.html", {"follows": user_follows, "followers": user_followers})
