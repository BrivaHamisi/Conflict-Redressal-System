# Generated by Django 4.1.1 on 2022-11-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_accounts', '0004_alter_generalissuesupdate_attached_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='documents',
            field=models.FileField(max_length=50, null=True, upload_to=''),
        ),
    ]