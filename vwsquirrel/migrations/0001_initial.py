# Generated by Django 2.2.7 on 2019-12-01 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='squirrel_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.IntegerField()),
                ('Longitude', models.IntegerField()),
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
    ]