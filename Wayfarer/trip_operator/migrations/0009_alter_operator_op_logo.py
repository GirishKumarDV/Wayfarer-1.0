# Generated by Django 3.2.12 on 2023-03-06 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_operator', '0008_auto_20230306_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='op_logo',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
    ]
