# Generated by Django 3.1.1 on 2020-09-16 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200916_1054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'sa', 'verbose_name_plural': 'sa'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='sihwan_user',
        ),
    ]
