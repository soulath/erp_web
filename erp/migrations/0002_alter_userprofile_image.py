# Generated by Django 4.2.4 on 2023-08-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='gallery/11_4773d101-9fd9-4a3b-944e-7c28a4ca7faa_800x800_wKpKBJb.webp', upload_to='gallery'),
        ),
    ]
