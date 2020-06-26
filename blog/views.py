from datetime import datetime
from itertools import chain

from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, reverse
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.generic import TemplateView

from blog.forms import ContactForm
from .models import Category, Event, Post, Talk, Tip


def get_categories():
    categories = Category.objects.all()
    return categories


def tips():
    tip = Tip.objects.get()
    return tip


def home(request):
    categories = get_categories()

    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    paginator = Paginator(post_list, 5)  # Show 5 posts per page
    page = request.GET.get('page')
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
        'blog/blog.html',
        {
            'title': 'Home',
            'year': datetime.now().year,
            'categories': categories,
            'posts': posts,
        }
    )


def talks(request):
    categories = get_categories()
    talk_list = Talk.objects.all().order_by('-pk')

    paginator = Paginator(talk_list, 5)  # Show 5 talks per page
    page = request.GET.get('page')
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
        'blog/talks.html',
        {
            'categories': categories,
            'title': 'Talks',
            'year': datetime.now().year,
            'talks': talks
        }
    )


def upcoming_events(request):
    categories = get_categories()
    event_list = Event.objects.filter(ispast=False).order_by('fromdate')

    paginator = Paginator(event_list, 5)  # Show 5 events per page
    page = request.GET.get('page')
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
        'blog/upcoming_events.html',
        {
            'categories': categories,
            'title': 'Upcoming Events',
            'year': datetime.now().year,
            'events': events,
        }
    )


def past_events(request):
    categories = get_categories()
    past_event_list = Event.objects.filter(ispast=True).order_by('-fromdate')

    paginator = Paginator(past_event_list, 5)  # Show 5 events per page
    page = request.GET.get('page')
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
        'blog/past_events.html',
        {
            'categories': categories,
            'title': 'Past Events',
            'year': datetime.now().year,
            'events': events,
        }
    )


class TalkView(TemplateView):
    template_name = "blog/talk.html"

    def get_context_data(self, pk, **kwargs):
        context = super(TalkView, self).get_context_data(**kwargs)
        context['categories'] = get_categories()
        context['talk'] = get_object_or_404(Talk, pk=pk)
        context['title'] = 'Talk'
        context['year'] = datetime.now().year
        return context


class ContactView(TemplateView):
    contact_form = ContactForm()
    template_name = "blog/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['categories'] = get_categories()
        contact_form = ContactForm()
        context['contact_form'] = contact_form
        context['title'] = 'Contact Details'
        context['year'] = datetime.now().year
        return context

    def post(self, request):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            details = contact_form.cleaned_data['message']

            message = render_to_string('emails/enquiry_email.html',
                                       {
                                           'name': name,
                                           'phone': phone,
                                           'email': email,
                                           'details': details,
                                           'subject': subject
                                       })

            from_email = None
            to_email = ['anna@makarudze.com']
            send_mail(subject, message, from_email, to_email)

            # redirect to a new URL:
            return reverse('blog:thankyou')


class ThankYouView(TemplateView):
    template_name = "blog/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super(ThankYouView, self).get_context_data(**kwargs)
        context['categories'] = get_categories()
        context['title'] = ''
        context['year'] = datetime.now().year
        return context


class PostView(TemplateView):
    template_name = "blog/post.html"

    def get_context_data(self, pk, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['categories'] = get_categories()
        context['post'] = get_object_or_404(Post, pk=pk)
        context['title'] = ''
        context['year'] = datetime.now().year
        return context


def posts_by_category(request, id):
    categories = get_categories()
    category = Category.objects.get(id=id)

    post_list = Post.objects.filter(category=id).order_by('-published_date')

    paginator = Paginator(post_list, 5)  # Show 5 posts per page
    page = request.GET.get('page')
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
        'blog/blog.html',
        {
            'title': category.name,
            'year': datetime.now().year,
            'categories': categories,
            'posts': posts,
        }
    )


def search(request, query):
    categories = get_categories()
    posts = Post.objects.filter(Q(title__contains=query) |
                                Q(text__contains=query))
    talks = Talk.objects.filter(Q(title__contains=query) | Q(description__contains=query))
    results_list = chain(posts, talks)

    paginator = Paginator(results_list, 5)  # Show 5 posts per page
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        results = paginator.page(paginator.num_pages)
    return render(
        request,
        'blog/search.html',
        {
            'title': f'Search results for {query}',
            'year': datetime.now().year,
            'categories': categories,
            'results': results,
        }
    )
