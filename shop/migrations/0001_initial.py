# Generated by Django 4.1.5 on 2023-03-17 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(db_index=True, max_length=128)),
                ('slug', models.SlugField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
                'ordering': ('brand_name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(db_index=True, max_length=128)),
                ('slug', models.SlugField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(db_index=True, max_length=256)),
                ('slug', models.SlugField(max_length=256)),
                ('image', models.ImageField(blank=True, upload_to='static/assets/productimages/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('usage', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.category')),
            ],
            options={
                'ordering': ('product_name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
