# Generated by Django 5.0.6 on 2024-09-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('company_type', models.CharField(choices=[('IT', 'IT'), ('Non-IT', 'Non-IT'), ('Manufacturing', 'Manufacturing')], max_length=100)),
                ('added_data', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
