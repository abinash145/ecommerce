# Generated by Django 3.2.4 on 2021-06-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_slider_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='status',
            field=models.BooleanField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default=False),
        ),
        migrations.AlterField(
            model_name='slider',
            name='rank',
            field=models.IntegerField(),
        ),
    ]
