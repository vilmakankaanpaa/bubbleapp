# Generated by Django 2.1.7 on 2019-03-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bubbleapp', '0007_auto_20190318_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='createDate',
            field=models.DateTimeField(verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='updateDate',
            field=models.DateTimeField(verbose_name='Updated'),
        ),
    ]