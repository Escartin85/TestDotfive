# Generated by Django 3.0 on 2021-04-06 14:44

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.CharField(choices=[('Category1', 'Category 1'), ('Category2', 'Category 2'), ('Category3', 'Category 3')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-label', '-date_created'],
            },
            managers=[
                ('items', django.db.models.manager.Manager()),
            ],
        ),
    ]
