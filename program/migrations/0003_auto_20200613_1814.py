# Generated by Django 2.2.10 on 2020-06-13 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_auto_20200607_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='duration',
            field=models.CharField(choices=[('S', '25min'), ('L', '40min')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='program.ProgramCategory'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='duration',
            field=models.CharField(choices=[('S', '25min'), ('L', '40min')], max_length=1),
        ),
    ]