# Generated by Django 4.1.1 on 2022-09-21 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_accounts', '0002_registrationform'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='Department',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
