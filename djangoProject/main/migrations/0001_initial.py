# Generated by Django 4.2.2 on 2023-06-27 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=64)),
                ('owner_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('booth_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.booth')),
                ('cream_type', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('size', models.CharField(max_length=16)),
            ],
            bases=('main.booth',),
        ),
    ]
