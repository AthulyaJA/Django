# Generated by Django 3.1.7 on 2021-03-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=200)),
                ('dis', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]