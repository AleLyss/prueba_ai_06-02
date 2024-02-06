# Generated by Django 5.0.1 on 2024-01-15 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_profile_cedula_alter_profile_direccion_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rol',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.RemoveField(
            model_name='carrito',
            name='id_cliente',
        ),
        migrations.RemoveField(
            model_name='carrito',
            name='id_producto',
        ),
        migrations.RemoveField(
            model_name='detalleingreso',
            name='id_ingreso',
        ),
        migrations.RemoveField(
            model_name='detalleingreso',
            name='id_producto',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='id_producto',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='id_venta',
        ),
        migrations.RemoveField(
            model_name='ingreso',
            name='id_proveedor',
        ),
        migrations.RemoveField(
            model_name='ingreso',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='id_cliente',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='id_usuario',
        ),
        migrations.AddField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.cliente'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.producto'),
        ),
        migrations.AddField(
            model_name='detalleingreso',
            name='ingreso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.ingreso'),
        ),
        migrations.AddField(
            model_name='detalleingreso',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.producto'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.producto'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.venta'),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.proveedor'),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.profile'),
        ),
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.cliente'),
        ),
        migrations.AddField(
            model_name='venta',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.profile'),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='id_telegram',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.telegram'),
        ),
    ]
