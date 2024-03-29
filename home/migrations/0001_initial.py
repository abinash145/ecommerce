# Generated by Django 3.2.4 on 2021-06-28 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('slug', models.CharField(max_length=500)),
                ('image', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('slug', models.CharField(max_length=500)),
                ('image', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('slug', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField(blank=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=40)),
                ('stock', models.CharField(blank=True, choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=50)),
                ('labels', models.CharField(blank=True, choices=[('new', 'new'), ('hot', 'hot'), ('sale', 'sale'), ('', 'default')], max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
            ],
        ),
    ]
