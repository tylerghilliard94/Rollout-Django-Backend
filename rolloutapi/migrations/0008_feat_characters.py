# Generated by Django 3.2.9 on 2022-07-26 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rolloutapi', '0007_spell_characters'),
    ]

    operations = [
        migrations.AddField(
            model_name='feat',
            name='characters',
            field=models.ManyToManyField(related_name='feats', to='rolloutapi.Character'),
        ),
    ]
