# Generated by Django 5.1.2 on 2024-10-27 07:27

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=225)),
                ('published_on', models.DateField()),
                ('is_borrowed', models.BooleanField(default=False)),
                ('add_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='added_books', to='library.users')),
                ('borrowed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='borrowed_by', to='library.users')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
