# Generated by Django 3.2.7 on 2021-10-01 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MeetUps', '0006_interns_organizoremail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interns',
            old_name='participant',
            new_name='participants',
        ),
    ]