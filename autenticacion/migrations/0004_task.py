# Generated by Django 4.1.5 on 2023-01-26 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0003_alumno_maestro_materia_remove_task_project_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacion.alumno')),
            ],
        ),
    ]
