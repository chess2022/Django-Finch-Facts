# Generated by Django 4.0.6 on 2022-07-14 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_finch_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='sighting date')),
                ('type', models.CharField(choices=[('S', 'Physically Seen'), ('H', 'Heard Song')], default='S', max_length=1)),
                ('finch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.finch')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
