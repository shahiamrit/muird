# Generated by Django 4.1.7 on 2023-02-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_iru_photo_alter_iru_par'),
    ]

    operations = [
        migrations.AddField(
            model_name='iru',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
