# Generated by Django 3.2.16 on 2023-01-18 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230118_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devtool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('kind', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
