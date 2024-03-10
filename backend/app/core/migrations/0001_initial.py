# Generated by Django 3.2.18 on 2024-03-10 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('uid', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=50)),
                ('description_filter_html', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('web_sales', models.URLField(blank=True, null=True)),
                ('source_web_promote', models.URLField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('edit_modify_date', models.DateTimeField()),
                ('source_web_name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('hit_rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('location_name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=255)),
                ('unit_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UnitActivityLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.activity')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unit')),
            ],
        ),
        migrations.CreateModel(
            name='ShowInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('on_sales', models.CharField(max_length=1)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('end_time', models.DateTimeField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_infos', to='core.activity')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.location')),
            ],
        ),
    ]