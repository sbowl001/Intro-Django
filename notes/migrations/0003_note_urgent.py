# Generated by Django 2.1.3 on 2018-11-08 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_remove_note_urgent'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='urgent',
            field=models.BooleanField(default=False),
        ),
    ]
