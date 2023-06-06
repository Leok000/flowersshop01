# Generated by Django 4.2.1 on 2023-05-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(null=True, upload_to='uploads')),
                ('in_stock', models.BooleanField(default=True)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
    ]
