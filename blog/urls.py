from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='blog'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
    path('category/<int:id>/', views.posts_by_category, name='category'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('past_events/', views.past_events, name='past_events'),
    path('upcoming_events/', views.upcoming_events, name='upcoming_events'),
    path('talks/', views.talks, name='talks'),
    path('talk/<int:pk>/', views.TalkView.as_view(), name='talk'),
    path('thankyou/', views.ThankYouView.as_view(), name='thankyou'),
    path('search/<str:query>/', views.search, name='search'),
    ]
