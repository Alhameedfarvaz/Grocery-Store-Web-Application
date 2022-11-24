# Generated by Django 3.0.3 on 2020-04-26 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_to_cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=30)),
                ('total_bill', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Product_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('category_name', models.CharField(max_length=20)),
                ('product_img1', models.ImageField(upload_to='pics')),
                ('product_img2', models.ImageField(upload_to='pics')),
                ('product_description', models.TextField(max_length=5000, null=True)),
                ('product_price', models.IntegerField()),
                ('product_expirydate', models.DateField(null=True)),
                ('product_manufecturingdate', models.DateField(null=True)),
                ('quantity', models.IntegerField(default=10)),
            ],
        ),
    ]
