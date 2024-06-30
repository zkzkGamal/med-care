# Generated by Django 4.1.1 on 2023-06-01 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0002_profile_user_alter_profile_medicaltype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='medicalType',
            field=models.TextField(choices=[('Hospital', 'Hospital'), ('Lab', 'Lab'), ('Petiant', 'Petiant'), ('Clinic', 'Clinic')], default='Petiant'),
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('specialist', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='photo')),
                ('years_of_experience', models.IntegerField(blank=True, max_length=2, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('reception', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medical_app.profile')),
            ],
        ),
    ]
