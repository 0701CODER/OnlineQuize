# Generated by Django 2.2.4 on 2020-03-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('option1', models.CharField(max_length=255, verbose_name='Option1')),
                ('option2', models.CharField(max_length=255, verbose_name='Option2')),
                ('option3', models.CharField(max_length=255, verbose_name='Option3')),
                ('option4', models.CharField(max_length=255, verbose_name='Option1')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
            ],
        ),
        migrations.CreateModel(
            name='StaffDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=255, verbose_name='Staff Name')),
                ('email_id', models.EmailField(max_length=255, verbose_name='Email Id')),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mobile Number')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('country', models.CharField(default='India', max_length=100, verbose_name='Country')),
                ('state', models.CharField(default='Tamil Nadu', max_length=100, verbose_name='State')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255, verbose_name='Student Name')),
                ('email_id', models.EmailField(max_length=255, verbose_name='Email Id')),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mobile Number')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('country', models.CharField(default='India', max_length=100, verbose_name='Country')),
                ('state', models.CharField(default='Tamil Nadu', max_length=100, verbose_name='State')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('university_no', models.CharField(max_length=100, unique=True, verbose_name='University No')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
            ],
        ),
    ]
