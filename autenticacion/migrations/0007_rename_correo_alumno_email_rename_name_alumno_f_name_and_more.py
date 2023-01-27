# Generated by Django 4.1.5 on 2023-01-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0006_delete_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='correo',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='name',
            new_name='f_name',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='cedula',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='telf',
        ),
        migrations.AddField(
            model_name='alumno',
            name='l_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='password',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='username',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
