from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.conf import settings
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import get_object_or_404, render, reverse
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.generic import TemplateView

import requests

from blog.forms import ContactForm
from .models import Category, Event, Post, Talk


def blog(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )

    paginator = Paginator(post_list, 5)  # Show 5 posts per page
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        "blog/blog.html",
        {
            "title": "Welcome to my Blog!",
            "posts": posts,
        },
    )


def home(request):
    return render(request, "blog/index.html", {"title": "For Hire"})


def about(request):
    return render(
        request,
        "blog/about.html",
        {
            "title": "About me",
        },
    )


def talks(request):
    talk_list = Talk.objects.all().order_by("-pk")

    paginator = Paginator(talk_list, 5)  # Show 5 talks per page
    page = request.GET.get("page")
    try:
        talks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        talks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        talks = paginator.page(paginator.num_pages)
    return render(
        request,
        "blog/talks.html",
        {
            "title": "Talks",
            "talks": talks,
        },
    )


def upcoming_events(request):
    event_list = Event.objects.future()

    paginator = Paginator(event_list, 5)  # Show 5 events per page
    page = request.GET.get("page")
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page(paginator.num_pages)
    return render(
        request,
        "blog/upcoming_events.html",
        {
            "title": "Upcoming Events",
            "events": events,
        },
    )


def past_events(request):
    past_event_list = Event.objects.past()

    paginator = Paginator(past_event_list, 5)  # Show 5 events per page
    page = request.GET.get("page")
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page(paginator.num_pages)
    return render(
        request,
        "blog/past_events.html",
        {
            "title": "Past Events",
            "events": events,
        },
    )


class TalkView(TemplateView):
    template_name = "blog/talk.html"

    def get_context_data(self, uuid, **kwargs):
        context = super(TalkView, self).get_context_data(**kwargs)
        context["talk"] = get_object_or_404(Talk, uuid=uuid)
        context["title"] = context["talk"].title
        return context


class ContactView(TemplateView):
    form = ContactForm()
    template_name = "blog/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        form = ContactForm()
        context["form"] = form
        context["title"] = "Contact Details"
        return context

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            recaptcha_response = request.POST.get("g-recaptcha-response")
            data = {
                "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                "response": recaptcha_response,
            }
            r = requests.post(
                "https://www.google.com/recaptcha/api/siteverify", data=data
            )
            result = r.json()

            if result["success"]:
                form.save()
                name = form.cleaned_data["name"]
                phone = form.cleaned_data["phone"]
                email = form.cleaned_data["email"]
                subject = form.cleaned_data["subject"]
                details = form.cleaned_data["message"]

                message = render_to_string(
                    "emails/enquiry_email.html",
                    {
                        "name": name,
                        "phone": phone,
                        "email": email,
                        "details": details,
                        "subject": subject,
                    },
                )

                from_email = None
                to_email = ["anna@makarudze.com"]
                try:
                    send_mail(subject, message, from_email, to_email)
                except BadHeaderError:
                    return HttpResponse("Invalid header found.")
                # redirect to a new URL:
                return reverse("blog:thankyou")


class ThankYouView(TemplateView):
    template_name = "blog/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super(ThankYouView, self).get_context_data(**kwargs)
        context["title"] = "Thank You"
        return context


class PostView(TemplateView):
    template_name = "blog/post.html"

    def get_context_data(self, slug, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, slug=slug)
        context["title"] = "Blog Post"
        return context


def posts_and_talks_by_category(request, id):
    category = Category.objects.get(id=id)
    posts_list = Post.objects.filter(category=id).order_by("-created_date")
    talks_list = Talk.objects.filter(category=id).order_by("-date_presented")

    return render(
        request,
        "blog/category.html",
        {
            "title": category.name,
            "posts_list": posts_list,
            "talks_list": talks_list,
        },
    )


def search(request):
    if request.GET.get("search_query") != None:
        search_query = request.GET.get("search_query")
        posts_search_results = Post.objects.filter(
            Q(title__contains=search_query)
            | Q(text__contains=search_query)
            | Q(category__name__icontains=search_query)
        ).order_by("-created_date")
        talks_search_results = Talk.objects.filter(
            Q(title__contains=search_query)
            | Q(description__contains=search_query)
            | Q(category__name__icontains=search_query)
        ).order_by("-date_presented")

        count = len(posts_search_results) + len(talks_search_results)

    else:
        count = 0
        search_query = ""
        posts_search_results = None
        posts_search_results = None

    return render(
        request,
        "blog/search.html",
        {
            "title": f'{count} search result(s) for "{search_query}"',
            "posts_search_results": posts_search_results,
            "talks_search_results": posts_search_results,
        },
    )
