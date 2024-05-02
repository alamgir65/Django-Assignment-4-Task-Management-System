# Generated by Django 5.0.4 on 2024-05-02 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=100)),
                ('taskDescription', models.TextField()),
                ('is_Completed', models.BooleanField(default=False)),
                ('taskAssignedDate', models.DateField(default=datetime.datetime(2024, 5, 3, 2, 37, 28, 578332))),
                ('categories', models.ManyToManyField(to='category.categorymodel')),
            ],
        ),
    ]
