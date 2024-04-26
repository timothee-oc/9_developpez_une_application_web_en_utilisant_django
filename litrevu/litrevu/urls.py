"""
URL configuration for litrevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import login_view, logout_view, signup_view
from review.views import feed_view, create_ticket, update_ticket, delete_ticket, create_review, update_review, delete_review, follows_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('feed/', feed_view, name='feed'),
    path('tickets/create/', create_ticket, name='create_ticket'),
    path('tickets/<int:ticket_id>/update/', update_ticket, name='update_ticket'),
    path('tickets/<int:ticket_id>/delete/', delete_ticket, name='delete_ticket'),
    path('reviews/create/', create_review, name='create_review'),
    path('reviews/<int:review_id>/update/', update_review, name='update_review'),
    path('reviews/<int:review_id>/delete/', delete_review, name='delete_review'),
    path('follows/', follows_view, name="follows")
]
