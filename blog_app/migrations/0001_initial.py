# Generated by Django 3.2.9 on 2022-01-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('main_information', models.TextField()),
                ('image', models.ImageField(upload_to='blog/')),
                ('pub_date', models.DateField()),
            ],
        ),
    ]