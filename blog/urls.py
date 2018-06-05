from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<pk>\d+)/$', views.PostView.as_view(), name='post'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contact$', views.ContactView.as_view(), name='contact'),
    url(r'^past_events/', views.past_events, name='past_events'),
    url(r'^upcoming_events/', views.upcoming_events, name='upcoming_events'),
    url(r'^talks/$', views.talks, name='talks'),
    url(r'^talk/(?P<pk>\d+)/$', views.TalkView.as_view(), name='talk'),
    url(r'^thankyou$', views.ThankYouView.as_view(), name='thankyou'),
    ]
