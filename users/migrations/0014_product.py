# Generated by Django 5.0.6 on 2024-06-25 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_delete_userregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
