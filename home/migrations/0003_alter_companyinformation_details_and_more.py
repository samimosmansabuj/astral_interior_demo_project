# Generated by Django 5.1.4 on 2024-12-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_ourteam_email_alter_ourteam_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinformation',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourproject',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
