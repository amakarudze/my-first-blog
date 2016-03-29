# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_event_dateposted'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('picture', models.ImageField(max_length=200, upload_to='', blank=True, null=True)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('picture', models.ImageField(max_length=200, upload_to='', blank=True, null=True)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='title', editable=False, unique=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DjangoArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('picture', models.ImageField(max_length=200, upload_to='presentations', blank=True, null=True)),
                ('attachment', models.FileField(max_length=200, upload_to='presentations', blank=True, null=True)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='title', editable=False, unique=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('startdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start date')),
                ('enddate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='End date')),
                ('description', models.TextField()),
                ('website', models.TextField(blank=True, null=True)),
                ('comments', models.TextField()),
                ('created_dateposted', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date created')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PythonArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('picture', models.ImageField(max_length=200, upload_to='presentations', blank=True, null=True)),
                ('attachment', models.FileField(max_length=200, upload_to='presentations', blank=True, null=True)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='title', editable=False, unique=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post', db_constraint=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='dateposted',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date posted'),
        ),
        migrations.AlterField(
            model_name='event',
            name='fromdate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='from date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='todate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='to date'),
        ),
    ]
