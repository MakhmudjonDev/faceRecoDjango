# Generated by Django 5.0.6 on 2024-05-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('encoding', models.BinaryField()),
            ],
        ),
    ]
