from django.db import models
from django.utils import timezone

from autoslug import AutoSlugField
from djrichtextfield.models import RichTextField


LEVEL_CHOICES = [
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
    ('Expert', 'Expert')
]


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        managed = True
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, blank=True)
    text = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    cover = models.ImageField(default='http://placehold.it/750x300', upload_to='covers', blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField("full name", max_length=120)
    phone = models.CharField("phone number", max_length=30)
    email = models.CharField("email address", max_length=120)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    email_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    from_date = models.DateTimeField('from date', default=timezone.now)
    to_date = models.DateTimeField('to date', default=timezone.now)
    location = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    comments = models.TextField()
    date_posted = models.DateTimeField('Date posted', default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_past = models.BooleanField(default=True)
    is_displayed = models.BooleanField(default=False)
    cover = models.ImageField(default='http://placehold.it/750x300', upload_to='covers', blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def is_past_due(self):
        if timezone.now() > self.todate:
            return True
        return False


class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    code = models.URLField(verbose_name="demo code", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    presenter = models.CharField(max_length=200, default='')
    slides = models.URLField(verbose_name="slides URL")
    date_presented = models.DateTimeField(default=timezone.now)
    cover = models.ImageField(default='http://placehold.it/750x300', upload_to='covers', blank=True)
    alt_text = models.CharField(max_length=100, verbose_name="Alt Text", default="Post Cover")
    youtube_video = models.URLField(null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.title


class Tip(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    topic = models.CharField(max_length=200, default='Django')
    tip = RichTextField()

    def __str__(self):
        return self.topic
