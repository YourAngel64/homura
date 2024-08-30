# Generated by Django 5.1 on 2024-08-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('pfp', models.ImageField(null=True, upload_to='')),
                ('about_me', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
