# Generated by Django 3.0.3 on 2020-03-11 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20200311_2142'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set(),
        ),
    ]