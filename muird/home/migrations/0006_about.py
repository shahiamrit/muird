# Generated by Django 4.1.7 on 2023-02-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_vmgo'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('par', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
