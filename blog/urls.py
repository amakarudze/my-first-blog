from django.conf.urls import url, patterns
from . import views
from blog.views import (HomeView, Post_ListView, ContactView, EventsView,
                        AboutView, ThankYouView, Post_DetailView, TalksView,
                        Talk_DetailView)


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^post_list/', Post_ListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', Post_DetailView.as_view(), name='post_detail'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^events/', EventsView.as_view(), name='events'),
    url(r'^talks/$', TalksView.as_view(), name='talks'),
    url(r'^talk/(?P<pk>\d+)/$', Talk_DetailView.as_view(), name='talk_details'),
    url(r'^thankyou$', ThankYouView.as_view(), name='thankyou'),
    ]
