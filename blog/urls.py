from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .sitemaps import BlogSitemap, StaticViewSitemap

sitemaps = {"static": StaticViewSitemap, "blog": BlogSitemap}

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # path("blog/", views.blog, name="blog"),
    path("post/<slug>/", views.PostView.as_view(), name="post"),
    path("category/<int:id>/", views.posts_and_talks_by_category, name="category"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("past_events/", views.past_events, name="past_events"),
    path("upcoming_events/", views.upcoming_events, name="upcoming_events"),
    path("talks/", views.talks, name="talks"),
    path("talk/<uuid>/", views.TalkView.as_view(), name="talk"),
    path("thank_you/", views.ThankYouView.as_view(), name="thank_you"),
    path("search/", views.search, name="search"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="blog/txt/robots.txt", content_type="text/plain"
        ),
        name="robots",
    ),
]
