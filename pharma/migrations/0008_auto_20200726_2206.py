# Generated by Django 3.0.8 on 2020-07-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0007_auto_20200726_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=' static/img/1503549.jpg', upload_to='products/'),
        ),
    ]
