# Generated by Django 3.2.9 on 2022-07-20 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rolloutapi', '0005_auto_20220720_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='proficiency_bonus',
        ),
        migrations.RemoveField(
            model_name='defaultcharacter',
            name='proficiency_bonus',
        ),
    ]
