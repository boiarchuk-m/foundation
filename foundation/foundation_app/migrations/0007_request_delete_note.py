# Generated by Django 5.1.4 on 2025-01-02 20:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundation_app', '0006_note_delete_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='ПІБ')),
                ('military_unit_number', models.CharField(max_length=100, verbose_name='Номер військової частини')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефону')),
                ('request_text', models.TextField(verbose_name='Запит')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
