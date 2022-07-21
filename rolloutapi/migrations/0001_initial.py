# Generated by Django 3.2.9 on 2022-07-21 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('armor_class', models.IntegerField(default=10)),
                ('cost_gp', models.IntegerField(default=0)),
                ('cost_sp', models.IntegerField(default=0)),
                ('cost_cp', models.IntegerField(default=0)),
                ('str_minimum', models.IntegerField(default=10)),
                ('stealth_disadvantage', models.BooleanField(default=False)),
                ('weight', models.IntegerField(default=1)),
                ('custom', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('abbr_name', models.CharField(max_length=4)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('experience', models.IntegerField(default=0)),
                ('strength', models.IntegerField(default=10)),
                ('dexterity', models.IntegerField(default=10)),
                ('constitution', models.IntegerField(default=10)),
                ('intelligence', models.IntegerField(default=10)),
                ('wisdom', models.IntegerField(default=10)),
                ('charisma', models.IntegerField(default=10)),
                ('hit_points', models.IntegerField(default=8)),
                ('temp_hit_points', models.IntegerField(default=0)),
                ('armor_class', models.IntegerField(default=10)),
                ('alignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='rolloutapi.alignment')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('hit_dice', models.IntegerField(default=6)),
                ('image', models.CharField(max_length=100)),
                ('spellcasting_ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_classes', to='rolloutapi.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='DamageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('cost_gp', models.IntegerField(default=0)),
                ('cost_sp', models.IntegerField(default=0)),
                ('cost_cp', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=1)),
                ('quantity', models.IntegerField(default=0)),
                ('custom', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MagicSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('cost_gp', models.IntegerField(default=0)),
                ('cost_sp', models.IntegerField(default=0)),
                ('cost_cp', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=1)),
                ('range', models.IntegerField(default=3)),
                ('damage', models.CharField(max_length=5)),
                ('two_handed', models.BooleanField(default=False)),
                ('two_handed_damage', models.CharField(max_length=5)),
                ('ranged', models.BooleanField(default=False)),
                ('custom', models.BooleanField(default=False)),
                ('damage_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weapons', to='rolloutapi.damagetype')),
                ('weapon_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weapons', to='rolloutapi.weapontype')),
            ],
        ),
        migrations.CreateModel(
            name='SubRace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('strength_bonus', models.IntegerField()),
                ('dexterity_bonus', models.IntegerField()),
                ('constitution_bonus', models.IntegerField()),
                ('intelligence_bonus', models.IntegerField()),
                ('wisdom_bonus', models.IntegerField()),
                ('charisma_bonus', models.IntegerField()),
                ('size', models.CharField(max_length=10)),
                ('able_to_choose_1', models.BooleanField(default=False)),
                ('choosable_stat_num_1', models.IntegerField()),
                ('able_to_choose_2', models.BooleanField(default=False)),
                ('choosable_stat_num_2', models.IntegerField()),
                ('flight_capable', models.BooleanField(default=False)),
                ('speed', models.IntegerField(default=30)),
                ('flight_speed', models.IntegerField(default=30)),
                ('base_race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_races', to='rolloutapi.race')),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('range', models.CharField(max_length=8)),
                ('duration', models.CharField(max_length=8)),
                ('concentration', models.BooleanField(default=False)),
                ('ritual', models.BooleanField(default=False)),
                ('casting_time', models.CharField(max_length=8)),
                ('level', models.IntegerField(default=1)),
                ('dc_success', models.CharField(max_length=10)),
                ('damage_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spells', to='rolloutapi.damagetype')),
                ('dc_save', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spells', to='rolloutapi.attribute')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spells', to='rolloutapi.magicschool')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='rolloutapi.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='RolloutUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('profile_image', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gp', models.IntegerField()),
                ('sp', models.IntegerField()),
                ('cp', models.IntegerField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money', to='rolloutapi.character')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('r_user_recieving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_requests', to='rolloutapi.rolloutuser')),
                ('r_user_sending', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='rolloutapi.rolloutuser')),
            ],
        ),
        migrations.CreateModel(
            name='DefaultCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('experience', models.IntegerField(default=0)),
                ('strength', models.IntegerField(default=10)),
                ('dexterity', models.IntegerField(default=10)),
                ('constitution', models.IntegerField(default=10)),
                ('intelligence', models.IntegerField(default=10)),
                ('wisdom', models.IntegerField(default=10)),
                ('charisma', models.IntegerField(default=10)),
                ('hit_points', models.IntegerField(default=8)),
                ('armor_class', models.IntegerField(default=10)),
                ('alignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='default_characters', to='rolloutapi.alignment')),
                ('character_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='default_characters', to='rolloutapi.characterclass')),
                ('languages', models.ManyToManyField(related_name='default_characters', to='rolloutapi.Language')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='default_characters', to='rolloutapi.subrace')),
                ('skills', models.ManyToManyField(related_name='default_characters', to='rolloutapi.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='character_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='rolloutapi.characterclass'),
        ),
        migrations.AddField(
            model_name='character',
            name='languages',
            field=models.ManyToManyField(related_name='characters', to='rolloutapi.Language'),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='rolloutapi.subrace'),
        ),
        migrations.AddField(
            model_name='character',
            name='rollout_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='rolloutapi.rolloutuser'),
        ),
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(related_name='characters', to='rolloutapi.Skill'),
        ),
    ]
