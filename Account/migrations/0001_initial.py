# Generated by Django 3.2.23 on 2025-01-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=64)),
                ('balance', models.IntegerField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]
