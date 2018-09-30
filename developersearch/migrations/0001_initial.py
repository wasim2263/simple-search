# Generated by Django 2.1.1 on 2018-09-30 07:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'developers',
            },
        ),
        migrations.CreateModel(
            name='Interviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MinValueValidator(5)])),
                ('comment', models.TextField(max_length=500)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developersearch.Developers')),
            ],
            options={
                'db_table': 'interviews',
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=254, unique=True)),
                ('developer', models.ManyToManyField(to='developersearch.Developers')),
            ],
            options={
                'db_table': 'languages',
            },
        ),
        migrations.CreateModel(
            name='ProgrammingLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('developer', models.ManyToManyField(to='developersearch.Developers')),
            ],
            options={
                'db_table': 'programming_languages',
            },
        ),
    ]