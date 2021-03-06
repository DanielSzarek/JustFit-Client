# Generated by Django 3.0.4 on 2020-06-21 13:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientExercise',
            new_name='ClientActivity',
        ),
        migrations.AlterModelOptions(
            name='clientactivity',
            options={'verbose_name_plural': 'Client Activities'},
        ),
        migrations.AlterModelOptions(
            name='clientproduct',
            options={'verbose_name_plural': 'Client Products'},
        ),
        migrations.RenameField(
            model_name='clientactivity',
            old_name='id_exercise',
            new_name='id_activity',
        ),
        migrations.AddIndex(
            model_name='clientactivity',
            index=models.Index(fields=['user', 'id_activity', 'active'], name='activity_name_idx'),
        ),
        migrations.AddIndex(
            model_name='clientproduct',
            index=models.Index(fields=['user', 'id_product', 'active'], name='product_name_idx'),
        ),
    ]
