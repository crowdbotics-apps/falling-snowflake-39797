# Generated by Django 2.2.28 on 2023-04-09 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxStatuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusId', models.UUIDField()),
                ('statusName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationId', models.UUIDField()),
                ('locationName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Boxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boxId', models.UUIDField()),
                ('boxLocation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boxes_boxLocation', to='home.Locations')),
                ('boxStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boxes_boxStatus', to='home.BoxStatuses')),
            ],
        ),
    ]
