# Generated by Django 4.0.4 on 2022-06-24 13:51

from django.db import migrations
import markdownfield.models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0024_alter_tip_tip"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="text",
            field=markdownfield.models.MarkdownField(rendered_field="text_rendered"),
        ),
    ]
