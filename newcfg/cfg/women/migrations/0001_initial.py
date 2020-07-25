# Generated by Django 3.0.8 on 2020-07-25 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WSSomen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default=None, max_length=100)),
                ('lname', models.CharField(default=None, max_length=100)),
                ('location', models.CharField(default=None, max_length=200)),
                ('contact', models.CharField(default=None, max_length=10)),
                ('skillset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='women.Skills')),
            ],
        ),
    ]