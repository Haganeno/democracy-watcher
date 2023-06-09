# Generated by Django 4.2 on 2023-04-12 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ballot',
            name='applicants',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ballot',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='deputy',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vote',
            name='deputy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.deputy'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('ballot', 'deputy')},
        ),
    ]
