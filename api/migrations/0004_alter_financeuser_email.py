# Generated by Django 3.2.6 on 2021-08-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_amountdetails_lender_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
