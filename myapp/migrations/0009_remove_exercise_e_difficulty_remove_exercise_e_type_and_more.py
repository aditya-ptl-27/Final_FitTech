# Generated by Django 4.1.4 on 2023-06-27 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_exercise_e_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='e_difficulty',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='e_type',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='equipment',
        ),
    ]
