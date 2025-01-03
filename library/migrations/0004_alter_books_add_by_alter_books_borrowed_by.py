# Generated by Django 5.1.2 on 2024-10-27 15:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_users_managers_alter_users_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='add_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='books',
            name='borrowed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
