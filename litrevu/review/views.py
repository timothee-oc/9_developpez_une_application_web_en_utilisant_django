from django.shortcuts import render, redirect
from .forms import TicketForm, ReviewForm
from .models import Ticket, Review

def feed_view(request):
    ticket = Ticket.objects.get(id=2)
    review = Review.objects.get(id=1)

    return render(request, 'review/feed.html', {'ticket': ticket, 'review': review})

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