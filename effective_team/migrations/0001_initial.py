# Generated by Django 5.1.3 on 2024-12-11 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Team creator')),
                ('score', models.FloatField(verbose_name='Score')),
            ],
            options={
                'verbose_name': 'Creator',
                'verbose_name_plural': 'Creators',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Team name')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='effective_team.creator', verbose_name='Team creator')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Team member')),
                ('endurance', models.IntegerField(verbose_name='Member endurance')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='effective_team.team', verbose_name='Team')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TeamApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='effective_team.member', verbose_name='Member')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='effective_team.team', verbose_name='Team')),
            ],
            options={
                'verbose_name': 'Team Application',
                'verbose_name_plural': 'Teams Applications',
                'ordering': ['id'],
            },
        ),
    ]
