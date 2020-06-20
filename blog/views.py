from __future__ import absolute_import
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime

from blog.forms import ContactForm
from .models import Post, Event, Talk, Contact


def get_event():
    events = Event.objects.filter(ispast=False).order_by('fromdate')
    return events

def past_event():
    past_events = Event.objects.filter(ispast=True).order_by('-fromdate')
    return past_events


def home(request):
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
            'posts': posts,
        }
    )


def talks(request):
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
            'title': 'Talks',
            'year': datetime.now().year,
            'talks': talks
        }
    )


def upcoming_events(request):
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
            'title': 'Upcoming Events',
            'year': datetime.now().year,
            'events': events,
        }
    )


def past_events(request):
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
            'title': 'Past Events',
            'year': datetime.now().year,
            'events': events,
        }
    )


class TalkView(TemplateView):
    template_name = "blog/talk.html"

    def get_context_data(self, pk, **kwargs):
        context = super(TalkView, self).get_context_data(**kwargs)
        context['talk'] = get_object_or_404(Talk, pk=pk)
        context['title'] = 'Talk'
        context['year'] = datetime.now().year
        return context


class ContactView(TemplateView):
    contact_form = ContactForm()
    template_name = "blog/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        contact_form = ContactForm()
        context['contact_form'] = contact_form
        context['title'] = 'Contact Me'
        context['message'] = 'My Contact Details'
        context['year'] = datetime.now().year
        return context

    def post(self, request):
        contact_form = ContactForm(request.POST)
        contact_form.save()

        to = ['harare@pyladies.com']
        subject = request.POST.get('subject', '')
        details = request.POST.get('message', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone')
        name = request.POST.get('name')

        if contact_form.is_valid():
            # process the data in feedback_form.cleaned_data as required
            obj = Contact()  # gets new object
            obj.name = contact_form.cleaned_data['name']
            obj.phone = contact_form.cleaned_data['phone']
            obj.email = contact_form.cleaned_data['email']
            obj.subject = contact_form.cleaned_data['subject']
            obj.message = contact_form.cleaned_data['message']
            # finally save the object in db
            obj.save()

            # send email to infoharare@genaulabs.com
            subject = "Message on Contact Form - " + contact_form.cleaned_data['subject']
            message = 'A message was submitted on the website\n\n'
            message += 'Name: ' + contact_form.cleaned_data['name'] + '\n'
            message += 'Email: ' + contact_form.cleaned_data['email'] + '\n'
            message += 'Phone: ' + contact_form.cleaned_data['phone'] + '\n'
            message += 'Message:\n ' + contact_form.cleaned_data['message'] + '\n'

            sender = 'anntelebiz@gmail.com'

            recipient_list = ['anna@anntele.com']
            send_mail(subject, message, sender, recipient_list)

            # redirect to a new URL:
            return HttpResponseRedirect('thankyou')


class ThankYouView(TemplateView):
    template_name = "blog/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super(ThankYouView, self).get_context_data(**kwargs)
        context['title'] = 'Thank You'
        context['year'] = datetime.now().year
        return context


class PostView(TemplateView):
    template_name = "blog/post.html"

    def get_context_data(self, pk, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=pk)
        context['title'] = 'Blog Post'
        context['year'] = datetime.now().year
        return context
