# Generated by Django 3.1.1 on 2020-09-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=34, verbose_name='사옹자명'),
        ),
    ]
