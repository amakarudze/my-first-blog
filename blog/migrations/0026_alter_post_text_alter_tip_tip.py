# Generated by Django 4.0.4 on 2022-06-24 14:20

from django.db import migrations
import markdownfield.models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0025_alter_post_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="text",
            field=markdownfield.models.MarkdownField(
                rendered_field="text_rendered", use_editor=False
            ),
        ),
        migrations.AlterField(
            model_name="tip",
            name="tip",
            field=markdownfield.models.MarkdownField(
                rendered_field="text_rendered", use_editor=False
            ),
        ),
    ]
