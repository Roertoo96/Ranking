# Generated by Django 4.1 on 2022-08-22 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeerPong', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beerpongrankingtable',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
