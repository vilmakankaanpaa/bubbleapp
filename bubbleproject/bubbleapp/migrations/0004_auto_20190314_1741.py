# Generated by Django 2.1.7 on 2019-03-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bubbleapp', '0003_account_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date added'),
        ),
    ]