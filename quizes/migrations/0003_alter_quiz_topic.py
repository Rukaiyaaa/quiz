# Generated by Django 5.1.1 on 2024-09-30 01:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('quizes', '0002_alter_quiz_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]
