from django.contrib import admin
from .models import Ticket, Review, UserFollows

admin.site.register([Ticket, Review, UserFollows])
