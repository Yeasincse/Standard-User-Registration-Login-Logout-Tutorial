# Generated by Django 2.0 on 2017-12-12 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='shohag', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='rahim', max_length=100),
            preserve_default=False,
        ),
    ]
