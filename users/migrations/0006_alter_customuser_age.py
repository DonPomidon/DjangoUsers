# Generated by Django 5.0.6 on 2024-06-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
