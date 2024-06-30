# Generated by Django 4.1.1 on 2023-06-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0004_alter_doctor_image_alter_doctor_years_of_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicpics',
            name='pic',
            field=models.ImageField(upload_to='photo/clincPic'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='medicalType',
            field=models.TextField(choices=[('Clinic', 'Clinic'), ('Petiant', 'Petiant'), ('Hospital', 'Hospital'), ('Lab', 'Lab')], default='Petiant'),
        ),
    ]
