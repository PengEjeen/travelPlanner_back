# Generated by Django 5.0.3 on 2024-04-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('cells', models.JSONField(blank=True, null=True)),
                ('planner_id', models.CharField(max_length=20)),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
