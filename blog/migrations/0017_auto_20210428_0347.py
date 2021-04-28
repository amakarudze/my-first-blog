# Generated by Django 3.0.14 on 2021-04-28 01:47

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_post_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emaildate',
            new_name='email_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='dateposted',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='fromdate',
            new_name='from_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='isdisplayed',
            new_name='is_displayed',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='ispast',
            new_name='is_past',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='todate',
            new_name='to_date',
        ),
        migrations.AlterField(
            model_name='event',
            name='cover',
            field=models.ImageField(blank=True, default='http://placehold.it/750x300', upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='event',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, default='http://placehold.it/750x300', upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=djrichtextfield.models.RichTextField(),
        ),
        migrations.AlterField(
            model_name='talk',
            name='cover',
            field=models.ImageField(blank=True, default='http://placehold.it/750x300', upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='tip',
            name='tip',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
