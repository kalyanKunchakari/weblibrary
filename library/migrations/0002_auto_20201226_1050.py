# Generated by Django 2.2.16 on 2020-12-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pyr',
            field=models.IntegerField(null=True),
        ),
    ]