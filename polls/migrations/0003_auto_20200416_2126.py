# Generated by Django 3.0.5 on 2020-04-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200416_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(verbose_name='date pubilsed'),
        ),
    ]
