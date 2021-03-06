# Generated by Django 3.0.3 on 2020-06-24 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200624_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='http://placehold.it/750x300', upload_to='covers'),
        ),
        migrations.AddField(
            model_name='talk',
            name='cover',
            field=models.ImageField(default='http://placehold.it/750x300', upload_to='covers'),
        ),
    ]
