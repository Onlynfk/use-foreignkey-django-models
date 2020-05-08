# Generated by Django 2.2 on 2020-04-24 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birth_date', models.DateTimeField()),
                ('weight', models.CharField(max_length=10)),
                ('height', models.CharField(max_length=10)),
                ('parent_name', models.CharField(max_length=200)),
                ('parent_mobile', models.CharField(max_length=16)),
                ('home_address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('date_immunized', models.DateTimeField()),
                ('initial_date', models.DateTimeField()),
                ('disease_type', models.CharField(max_length=30)),
                ('vaccine_type', models.CharField(max_length=30)),
                ('position', models.IntegerField()),
                ('child_record', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Record')),
            ],
        ),
    ]
