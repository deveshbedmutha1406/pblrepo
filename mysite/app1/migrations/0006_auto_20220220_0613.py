# Generated by Django 2.2 on 2022-02-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_applications_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='app1/static/imagedata'),
        ),
    ]
