# Generated by Django 3.2 on 2025-02-24 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20250224_2304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='off_shelevs_date',
            new_name='off_shelves_date',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='put_shelevs_date',
            new_name='put_shelves_date',
        ),
    ]
