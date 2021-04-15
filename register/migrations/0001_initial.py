# Generated by Django 3.2 on 2021-04-12 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('contact_number', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modification_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_supperuser', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='ExtractedRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_template', models.TextField()),
                ('recipe_url', models.TextField()),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modification_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('source', models.CharField(max_length=50)),
                ('recipe_title', models.CharField(max_length=50)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'extracted_recipe',
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=50)),
                ('recipeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.extractedrecipe')),
            ],
            options={
                'db_table': 'ingredients',
            },
        ),
    ]
