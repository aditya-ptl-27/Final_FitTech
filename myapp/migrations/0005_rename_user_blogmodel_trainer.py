# Generated by Django 4.1.4 on 2023-06-18 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_blogmodel_delete_bmi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmodel',
            old_name='user',
            new_name='trainer',
        ),
    ]