# Generated by Django 4.0.4 on 2022-05-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=700, null=True)),
                ('creators', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]