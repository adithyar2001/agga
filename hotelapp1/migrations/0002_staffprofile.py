# Generated by Django 5.0.1 on 2024-02-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='staffprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('number', models.CharField(max_length=50, null=True)),
                ('age', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('address', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('username', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('confirm_password', models.CharField(max_length=50, null=True)),
                ('staff_id', models.CharField(max_length=20, unique=True)),
                ('approval', models.BooleanField(default=False)),
            ],
        ),
    ]