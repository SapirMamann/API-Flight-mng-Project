# Generated by Django 4.2.4 on 2023-08-06 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0011_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserGroup',
        ),
        migrations.AlterModelOptions(
            name='administrator',
            options={'permissions': [('add_logentry', 'Can manage administrators')]},
        ),
        migrations.AlterModelOptions(
            name='airlinecompany',
            options={'permissions': [('can_manage_airline_companies', 'Can manage airline companies')]},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': [('can_manage_administrators', 'Can manage administrators')]},
        ),
    ]
