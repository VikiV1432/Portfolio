# Generated by Django 5.1.1 on 2024-10-19 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_about_alter_education_options_education_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=models.TextField(),
        ),
    ]
