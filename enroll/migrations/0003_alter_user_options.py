# Generated by Django 3.2.3 on 2021-05-17 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20210517_1926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['roll']},
        ),
    ]
