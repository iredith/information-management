# Generated by Django 3.1.2 on 2020-10-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_student', '0005_auto_20201017_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stream',
            field=models.IntegerField(choices=[(0, 'cse'), (1, 'ece')], default=0),
        ),
    ]
