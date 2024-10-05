# Generated by Django 5.1.1 on 2024-09-30 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, max_length=120, null=True, unique=True)),
            ],
        ),
    ]
