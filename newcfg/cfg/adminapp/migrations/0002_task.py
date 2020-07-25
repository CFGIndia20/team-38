# Generated by Django 3.0.8 on 2020-07-25 10:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=500)),
                ('task_quantity', models.CharField(max_length=200)),
                ('task_description', models.CharField(max_length=500)),
                ('task_skill', models.CharField(choices=[('Skill1', 'Skill1'), ('Skill2', 'Skill2'), ('Skill3', 'Skill3')], default='Skill1', max_length=100)),
                ('task_total_hour', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Amount should be more than 0')])),
            ],
        ),
    ]