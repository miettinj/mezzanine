# Generated by Django 3.2 on 2022-12-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_types', '0002_alter_author_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dob',
            field=models.DateField(null=True, verbose_name='Date of birth'),
        ),
    ]
