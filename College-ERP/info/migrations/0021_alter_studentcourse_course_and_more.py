# Generated by Django 4.0.2 on 2022-02-18 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0020_feemanager_to_acno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='info.course'),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='info.student'),
        ),
    ]