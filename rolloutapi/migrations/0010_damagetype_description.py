# Generated by Django 3.2.9 on 2022-07-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rolloutapi', '0009_auto_20220720_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='damagetype',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]