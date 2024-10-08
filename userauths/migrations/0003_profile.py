# Generated by Django 5.1.1 on 2024-09-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile-image')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
