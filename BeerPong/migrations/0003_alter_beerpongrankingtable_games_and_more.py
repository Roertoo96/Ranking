# Generated by Django 4.0.6 on 2022-08-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeerPong', '0002_beerpongrankingtable_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beerpongrankingtable',
            name='games',
            field=models.IntegerField(default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='beerpongrankingtable',
            name='rank',
            field=models.IntegerField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='beerpongrankingtable',
            name='wins',
            field=models.IntegerField(default='0', max_length=5),
        ),
    ]
