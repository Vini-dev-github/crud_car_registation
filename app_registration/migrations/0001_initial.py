# Generated by Django 5.0.6 on 2024-05-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('ano', models.IntegerField()),
            ],
        ),
    ]