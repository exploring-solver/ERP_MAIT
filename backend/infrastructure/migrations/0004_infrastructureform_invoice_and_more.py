# Generated by Django 4.2.6 on 2023-12-03 19:21

from django.db import migrations, models
import infrastructure.utils


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0003_departmentrooms_departments_institutedepartments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='infrastructureform',
            name='invoice',
            field=models.FileField(blank=True, null=True, upload_to=infrastructure.utils.invoice_rename),
        ),
        migrations.AlterField(
            model_name='infrastructureform',
            name='year_of_purchase',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
