# Generated by Django 5.1.10 on 2025-06-08 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductosTerceros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField(default=1.0)),
                ('vendedor', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
