# Generated by Django 4.0.4 on 2022-04-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
