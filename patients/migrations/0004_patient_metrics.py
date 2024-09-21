# Generated by Django 5.1.1 on 2024-09-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_patient_bmi_patient_height_patient_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='metrics',
            field=models.CharField(choices=[('BP', 'Blood Pressure'), ('Sugar', 'Sugar Level'), ('Hemoglobin', 'Hemoglobin')], default='BP'),
        ),
    ]
