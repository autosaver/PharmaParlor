# Generated by Django 3.0.8 on 2020-07-26 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0010_auto_20200726_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='media/1503549.jpg', upload_to='product/'),
        ),
    ]
