from __future__ import absolute_import
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

from datetime import datetime

from blog.forms import ContactForm, CommentForm
from .models import (Post, Event, Article, AboutPage, DjangoArticle,
                     PythonArticle, Project)


def get_event():
    events = Event.objects.filter(ispast=False).order_by('-published_date')
    return events


class HomeView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        context['events'] = get_event()
        context['title'] = 'Home Page'
        context['year'] = datetime.now().year
        return context


class AboutView(TemplateView):
    template_name = "blog/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['aboutpage'] = AboutPage.objects.all()
        context['events'] = get_event()
        context['title'] = 'About Anna'
        context['year'] = datetime.now().year
        return context


class ProjectsView(TemplateView):
    template_name = "blog/projects.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all().order_by('-pk')
        context['events'] = get_event()
        context['title'] = 'Projects'
        context['year'] = datetime.now().year
        return context


class Project_DetailView(TemplateView):
    template_name = "blog/project_details.html"

    def get_context_data(self, pk, **kwargs):
        context = super(Project_DetailView, self).get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=pk)
        context['events'] = get_event()
        context['title'] = 'Projects'
        context['message'] = 'Projects'
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

        to = ['anna@anntele.com']
        subject = request.POST.get('subject', '')
        details = request.POST.get('message', '')
        email = request.POST.get('email', '')
        phone =  request.POST.get('phone')
        name = request.POST.get('name')

        ctx = {'name': name,
               'phone': phone,
               'email': email,
               'details': details,
               }

        if subject and details and email:
            try:
                message = render_to_string('emails/webenquiry.txt', ctx)
                EmailMessage(subject, message, to=to).send()
                return HttpResponseRedirect('thankyou')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')


class GalleryView(TemplateView):
    template_name = "blog/gallery.html"

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['title'] = 'My Work in Pictures'
        context['year'] = datetime.now().year
        return context


class EventsView(TemplateView):
    template_name = "blog/events.html"

    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        context['events'] = get_event()
        context['title'] = 'Upcoming Events'
        context['year'] = datetime.now().year
        return context


class PythonView(TemplateView):
    template_name = "blog/python.html"

    def get_context_data(self, **kwargs):
        context = super(PythonView, self).get_context_data(**kwargs)
        context['articles'] =  PythonArticle.objects.all()
        context['events'] = get_event()
        context['title'] = 'Python'
        context['year'] = datetime.now().year
        return context


class Python_DetailView(TemplateView):
    template_name = "blog/python_details.html"

    def get_context_data(self, pk, **kwargs):
        context = super(Python_DetailView, self).get_context_data(**kwargs)
        context['article'] = get_object_or_404(PythonArticle, pk=pk)
        context['events'] = get_event()
        context['title'] = 'Python'
        context['message'] = 'Python'
        context['year'] = datetime.now().year
        return context


class DjangoView(TemplateView):
    template_name = "blog/django.html"

    def get_context_data(self, **kwargs):
        context = super(DjangoView, self).get_context_data(**kwargs)
        context['articles'] = DjangoArticle.objects.all()
        context['events'] = get_event()
        context['title'] = 'Django'
        context['year'] = datetime.now().year
        return context


class Django_DetailView(TemplateView):
    template_name = "blog/django_details.html"

    def get_context_data(self, pk, **kwargs):
        context = super(Django_DetailView, self).get_context_data(**kwargs)
        context['article'] = get_object_or_404(DjangoArticle, pk=pk)
        context['events'] = get_event()
        context['title'] = 'Django'
        context['message'] = 'Django'
        context['year'] = datetime.now().year
        return context


class ThankYouView(TemplateView):
    template_name = "blog/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super(ThankYouView, self).get_context_data(**kwargs)
        context['title'] = 'Thank You'
        context['year'] = datetime.now().year
        return context


class Post_ListView(TemplateView):
    template_name = "blog/post_list.html"

    def get_context_data(self, **kwargs):
        context = super(Post_ListView, self).get_context_data(**kwargs)
        context['title'] = 'Blog Posts'
        context['year'] = datetime.now().year
        context['posts'] =  Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return context


class Post_DetailView(TemplateView):
    comment_form = CommentForm()
    template_name = "blog/post_detail.html"

    def get_context_data(self, pk, **kwargs):
        context = super(Post_DetailView, self).get_context_data(**kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        context['post'] = get_object_or_404(Post, pk=pk)
        context['title'] = 'My Blog'
        context['message'] = 'My Blog'
        context['year'] = datetime.now().year
        return context

    def post(self, request):
        comment_form = CommentForm(request.POST)
        comment_form.save()
