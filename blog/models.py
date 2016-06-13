from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
    default=timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)

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
    emaildate = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField("full name", max_length=120)
    email = models.CharField("email address", max_length=120)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)
    post = models.ForeignKey('Post', db_constraint=False)

    class Meta:
        managed = True

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Event(models.Model):
    name = models.CharField(max_length=200)
    fromdate = models.DateTimeField('from date', default=timezone.now)
    todate = models.DateTimeField('to date', default=timezone.now)
    location = models.CharField(max_length=200)
    website = models.TextField()
    comments = models.TextField()
    dateposted = models.DateTimeField('Date posted', default=timezone.now)
    published_date = models.DateTimeField(
                                          blank=True, null=True)
    ispast = models.BooleanField(default=True)

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


class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    picture = models.ImageField(max_length=200, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(
    default=timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class AboutPage(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    picture = models.ImageField(max_length=200, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(
    default=timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class PythonArticle(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    picture = models.ImageField(upload_to='presentations', max_length=200, null=True, blank=True)
    attachment = models.FileField(upload_to='presentations', max_length=200, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(
    default=timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class DjangoArticle(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    picture = models.ImageField(upload_to='presentations', max_length=200, null=True, blank=True)
    attachment = models.FileField(upload_to='presentations', max_length=200, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(
    default=timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=200)
    startdate = models.DateTimeField('Start date', default=timezone.now)
    enddate = models.DateTimeField('End date', default=timezone.now)
    description =  models.TextField()
    website = models.TextField(null=True, blank=True)
    comments = models.TextField()
    created_dateposted = models.DateTimeField('Date created', default=timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()
