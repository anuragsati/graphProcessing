# Generated by Django 4.0.5 on 2022-06-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startNode', models.IntegerField(blank=True, null=True)),
                ('endNode', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
