# Generated by Django 2.2.8 on 2019-12-13 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
        migrations.AlterField(
            model_name='course',
            name='slots',
            field=models.IntegerField(verbose_name='vagas'),
        ),
    ]