# Generated by Django 2.2.7 on 2019-11-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191128_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('code', models.CharField(max_length=50, null=True, verbose_name='code')),
                ('level', models.CharField(max_length=50, null=True, verbose_name='level')),
            ],
        ),
    ]
