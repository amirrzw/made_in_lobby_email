# Generated by Django 3.2.7 on 2021-10-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
