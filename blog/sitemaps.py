from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from .models import Post


class StaticViewSitemap(Sitemap):
    def items(self):
        return ["blog:home", "blog:about", "blog:talks"]

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def location(self, item):
        url = item.slug
        return url

    def lastmod(self, obj):
        return obj.created

    def _urls(self, page, protocol, domain):
        return super(BlogSitemap, self)._urls(page=page, protocol="https", domain="")
