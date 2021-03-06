# Generated by Django 3.0.14 on 2021-04-28 13:55

from django.db import migrations
import markdownfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210428_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=markdownfield.models.MarkdownField(rendered_field='text_rendered', use_editor=False),
        ),
        migrations.AlterField(
            model_name='tip',
            name='tip',
            field=markdownfield.models.MarkdownField(rendered_field='text_rendered', use_editor=False),
        ),
    ]
