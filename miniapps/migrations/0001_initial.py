# Generated by Django 4.0 on 2021-12-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniApp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]