# Generated by Django 4.0.6 on 2022-07-19 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_region_remove_finch_region_finch_user_photo_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='Image',
        ),
        migrations.AlterField(
            model_name='image',
            name='sighting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.finch'),
        ),
    ]
