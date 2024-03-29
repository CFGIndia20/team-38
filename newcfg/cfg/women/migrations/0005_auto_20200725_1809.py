# Generated by Django 3.0.8 on 2020-07-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0004_women_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('curr_work', models.CharField(default=None, max_length=100)),
                ('hrperday', models.CharField(default=None, max_length=10)),
                ('nopro', models.CharField(default=None, max_length=10)),
                ('day', models.CharField(default=None, max_length=20)),
                ('img', models.FileField(default='default.jpg', upload_to='media/progression')),
            ],
        ),
        migrations.RemoveField(
            model_name='women',
            name='mail',
        ),
    ]
