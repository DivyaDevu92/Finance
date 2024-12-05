# Generated by Django 5.1.1 on 2024-11-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=20)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('account_type', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=255)),
                ('holder', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='busines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operational', models.FloatField()),
                ('employ', models.FloatField()),
                ('adv', models.FloatField()),
                ('sales', models.FloatField()),
                ('other', models.FloatField()),
                ('total', models.FloatField(default=0.0)),
                ('date_field', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='entertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.FloatField()),
                ('music', models.FloatField()),
                ('sports', models.FloatField()),
                ('gaming', models.FloatField()),
                ('book', models.FloatField()),
                ('hobby', models.FloatField()),
                ('event', models.FloatField()),
                ('other', models.FloatField()),
                ('total', models.FloatField(default=0.0)),
                ('date_field', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fresh', models.FloatField()),
                ('meat', models.FloatField()),
                ('sweets', models.FloatField()),
                ('fast', models.FloatField()),
                ('dairy', models.FloatField()),
                ('beverages', models.FloatField()),
                ('restaurants', models.FloatField()),
                ('pet', models.FloatField()),
                ('other', models.FloatField()),
                ('total', models.FloatField(default=0.0)),
                ('date_field', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicines', models.FloatField()),
                ('mental', models.FloatField()),
                ('physical', models.FloatField()),
                ('insurance', models.FloatField()),
                ('other', models.FloatField()),
                ('total', models.FloatField(default=0.0)),
                ('date_field', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.FloatField()),
                ('electricity', models.FloatField()),
                ('water', models.FloatField()),
                ('gas', models.FloatField()),
                ('sewage', models.FloatField()),
                ('internet', models.FloatField()),
                ('insurance', models.FloatField()),
                ('taxes', models.FloatField()),
                ('repairs', models.FloatField()),
                ('furnishings', models.FloatField()),
                ('security', models.FloatField()),
                ('other', models.FloatField()),
                ('total', models.FloatField(default=0.0)),
                ('date_field', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.FloatField()),
                ('supplies', models.FloatField()),
                ('uniforms', models.FloatField()),
                ('transportation', models.FloatField()),
                ('enrichment', models.FloatField()),
                ('other', models.FloatField()),
                ('total', models.FloatField(default=0.0)),
                ('date_field', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='shopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes', models.FloatField()),
                ('access', models.FloatField()),
                ('beauty', models.FloatField()),
                ('electronics', models.FloatField()),
                ('homeacs', models.FloatField()),
                ('sports', models.FloatField()),
                ('toys', models.FloatField()),
                ('other', models.FloatField()),
                ('total', models.FloatField(default=0.0)),
                ('date_field', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='socialservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.FloatField()),
                ('staff', models.FloatField()),
                ('operational', models.FloatField()),
                ('donation', models.FloatField()),
                ('transportation', models.FloatField()),
                ('legal', models.FloatField()),
                ('subsidies', models.FloatField()),
                ('health', models.FloatField()),
                ('other', models.FloatField()),
                ('total', models.FloatField(default=0.0)),
                ('date_field', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='travelling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportation', models.FloatField()),
                ('accommodation', models.FloatField()),
                ('insurance', models.FloatField()),
                ('visa', models.FloatField()),
                ('other', models.FloatField()),
                ('total', models.FloatField(default=0.0)),
                ('date_field', models.DateField(auto_now=True)),
            ],
        ),
    ]
