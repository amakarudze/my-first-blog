from django.contrib import admin
from .models import Category, Contact, Event, Post, Talk

admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Talk)

