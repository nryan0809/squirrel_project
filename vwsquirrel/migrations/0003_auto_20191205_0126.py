# Generated by Django 2.2.7 on 2019-12-05 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vwsquirrel', '0002_auto_20191201_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='sq_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Unique_Squirrel_ID', models.TextField()),
                ('Shift', models.TextField()),
                ('Date', models.TextField()),
                ('Age', models.TextField()),
                ('Primary_Fur_Color', models.TextField()),
                ('Location', models.TextField()),
                ('Specific_Location', models.TextField()),
                ('Running', models.BooleanField()),
                ('Chasing', models.BooleanField()),
                ('Climbing', models.BooleanField()),
                ('Eating', models.BooleanField()),
                ('Foraging', models.BooleanField()),
                ('Other_Activities', models.CharField(max_length=200)),
                ('Kuks', models.BooleanField()),
                ('Quaas', models.BooleanField()),
                ('Moans', models.BooleanField()),
                ('Tail_flags', models.BooleanField()),
                ('Tail_twitches', models.BooleanField()),
                ('Approaches', models.BooleanField()),
                ('Indifferent', models.BooleanField()),
                ('Runs_from', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='squ_model',
        ),
    ]
