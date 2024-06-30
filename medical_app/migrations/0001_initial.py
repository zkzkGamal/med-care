# Generated by Django 4.1.1 on 2023-06-01 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist_name', models.CharField(blank=True, max_length=10, null=True)),
                ('last_name', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('nationalID', models.IntegerField(blank=True, max_length=14, null=True)),
                ('medicalType', models.TextField(choices=[('Clinic', 'Clinic'), ('Petiant', 'Petiant'), ('Lab', 'Lab'), ('Hospital', 'Hospital')], default='Petiant')),
            ],
        ),
    ]
