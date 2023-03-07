# Generated by Django 4.1.7 on 2023-03-07 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(max_length=10)),
                ('merchant_id', models.IntegerField(max_length=10)),
                ('category_id', models.IntegerField(max_length=10)),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('calories', models.IntegerField(max_length=10)),
                ('product_image', models.CharField(max_length=128)),
                ('stock', models.IntegerField(max_length=10)),
                ('status', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=128)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]