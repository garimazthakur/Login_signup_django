# Generated by Django 4.0.4 on 2022-05-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]