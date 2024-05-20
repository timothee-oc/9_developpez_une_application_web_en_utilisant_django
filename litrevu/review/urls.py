from django.urls import path
from . import views

urlpatterns = [
    path("feed/", views.feed, name="feed"),
    path("posts/", views.posts, name="posts"),
    path("follows/", views.follows, name="follows"),
    path("follows/<int:follow_id>/delete/", views.delete_follow, name="delete_follow"),
    path("tickets/create/", views.create_ticket, name="create_ticket"),
    path("tickets/<int:ticket_id>/update/", views.update_ticket, name="update_ticket"),
    path("tickets/<int:ticket_id>/delete/", views.delete_ticket, name="delete_ticket"),
    path("reviews/create/", views.create_review_and_ticket, name="create_review_and_ticket"),
    path("reviews/create/ticket_<int:ticket_id>/", views.create_review, name="create_review"),
    path("reviews/<int:review_id>/update/", views.update_review, name="update_review"),
    path("reviews/<int:review_id>/delete/", views.delete_review, name="delete_review"),
]