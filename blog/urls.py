from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('past_events/', views.past_events, name='past_events'),
    path('upcoming_events/', views.upcoming_events, name='upcoming_events'),
    path('talks/', views.talks, name='talks'),
    path('talk/<int:pk>/', views.TalkView.as_view(), name='talk'),
    path('thankyou/', views.ThankYouView.as_view(), name='thankyou'),
    ]
