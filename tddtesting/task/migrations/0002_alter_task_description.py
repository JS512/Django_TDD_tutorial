# Generated by Django 4.2.9 on 2024-01-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
