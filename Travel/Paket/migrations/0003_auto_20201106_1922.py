# Generated by Django 3.1.1 on 2020-11-06 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Paket', '0002_auto_20201106_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagespaket',
            name='id_paket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Paket.modelpaket'),
        ),
    ]
