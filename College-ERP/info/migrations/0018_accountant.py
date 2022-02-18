# Generated by Django 4.0.2 on 2022-02-18 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0017_course_fees_teacher_salary_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
                ('DOB', models.DateField(default='1980-01-01')),
                ('salary', models.PositiveIntegerField(null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accountant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]