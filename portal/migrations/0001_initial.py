# Generated by Django 2.2.2 on 2019-06-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfraVltgDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asof', models.DateTimeField(blank=True)),
                ('environment', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('vltg_identity', models.CharField(max_length=200)),
                ('cvproduct', models.CharField(max_length=200)),
                ('cvapi', models.CharField(max_length=200)),
                ('srcip', models.CharField(max_length=200)),
                ('typeofapi', models.CharField(max_length=200)),
                ('hostname', models.CharField(max_length=200)),
                ('create_dt', models.DateTimeField(blank=True)),
            ],
        ),
    ]
