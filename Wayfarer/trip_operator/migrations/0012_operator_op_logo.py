# Generated by Django 3.2.12 on 2023-03-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_operator', '0011_remove_operator_op_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='op_logo',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
