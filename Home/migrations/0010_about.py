# Generated by Django 5.1 on 2024-08-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_remove_agents_agents_desc2'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About_icone', models.CharField(max_length=100)),
                ('About_desc1', models.CharField(max_length=200)),
                ('paragraph_text', models.TextField()),
                ('About_name', models.CharField(max_length=50)),
                ('About_desc2', models.TextField()),
            ],
        ),
    ]
