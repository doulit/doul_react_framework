# Generated by Django 2.2.7 on 2019-11-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20191128_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='link',
            field=models.CharField(max_length=200, null=True, verbose_name='link'),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_parent',
            field=models.CharField(max_length=50, null=True, verbose_name='menu_parent'),
        ),
    ]
