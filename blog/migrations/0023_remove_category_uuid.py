# Generated by Django 4.0.4 on 2022-06-24 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0022_category_uuid_talk_uuid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="uuid",
        ),
    ]
