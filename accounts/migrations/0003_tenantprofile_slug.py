# Generated by Django 5.0 on 2023-12-25 14:03

import django_extensions.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_tenantprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantprofile',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='Automatically generated slug based on the name.', populate_from='name'),
        ),
    ]
