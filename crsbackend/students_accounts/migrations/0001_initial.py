# Generated by Django 4.1.1 on 2022-09-18 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintsForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complain_description', models.CharField(max_length=100)),
                ('Events_that_took_Place', models.TextField()),
                ('Consequence_suffered', models.TextField()),
                ('Spoken_to_someone', models.TextField()),
                ('Dissatisfied_with_Informal_complaint', models.TextField()),
                ('evidence', models.TextField()),
                ('recommendation', models.TextField()),
                ('date', models.TextField()),
                ('status_of_complaint', models.TextField()),
            ],
        ),
    ]
