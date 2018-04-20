# Generated by Django 2.0.3 on 2018-04-20 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_trips', to='travel_app.User')),
                ('users', models.ManyToManyField(related_name='trips', to='travel_app.User')),
            ],
        ),
    ]
