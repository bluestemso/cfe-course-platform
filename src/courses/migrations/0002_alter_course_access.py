# Generated by Django 5.1.5 on 2025-01-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='access',
            field=models.CharField(choices=[('any', 'Anyone'), ('email_required', 'Email Required')], default='email_required', max_length=14),
        ),
    ]
