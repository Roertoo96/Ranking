# Generated by Django 4.0.6 on 2022-08-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeerPongRankingTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(default='', max_length=30)),
                ('username', models.CharField(default='', max_length=30)),
                ('wins', models.CharField(default='', max_length=30)),
                ('games', models.CharField(default='', max_length=30)),
            ],
        ),
    ]