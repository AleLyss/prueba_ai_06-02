# Generated by Django 5.0.1 on 2024-01-15 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_delete_rol_delete_usuario_remove_carrito_id_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_telegram',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.telegram'),
        ),
    ]