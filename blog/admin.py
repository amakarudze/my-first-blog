from django.contrib import admin
from .models import Post, Contact, Event, Talk

admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Talk)

