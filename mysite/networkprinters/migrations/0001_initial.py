# Generated by Django 3.2.7 on 2021-10-09 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=300, null=True)),
                ('company', models.CharField(default='', max_length=300, null=True)),
                ('designation', models.CharField(default='', max_length=300, null=True)),
                ('email', models.EmailField(default='', max_length=300, null=True)),
                ('feedback', models.CharField(default='', max_length=600, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('mail_id', models.EmailField(blank=True, max_length=200, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('email_validate_limit', models.IntegerField(default=50)),
                ('job_portal_limit', models.IntegerField(default=15)),
                ('company_details_limit', models.IntegerField(default=5)),
                ('person_details_limit', models.IntegerField(default=50)),
                ('domain_details_limit', models.IntegerField(default=20)),
                ('profile_pic', models.ImageField(blank=True, default='profile.png', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]