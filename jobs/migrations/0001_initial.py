# Generated by Django 2.2.2 on 2019-06-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('jobdate', models.DateTimeField()),
                ('body', models.TextField()),
            ],
        ),
    ]
