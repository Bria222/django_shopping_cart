# Generated by Django 3.1.2 on 2021-04-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='more',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
