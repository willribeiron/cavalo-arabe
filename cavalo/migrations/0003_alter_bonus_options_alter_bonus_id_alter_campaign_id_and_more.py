# Generated by Django 4.1.5 on 2023-01-18 17:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cavalo', '0002_alter_bonus_id_alter_campaign_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bonus',
            options={'verbose_name': 'Bonus', 'verbose_name_plural': 'Bonus'},
        ),
        migrations.AlterField(
            model_name='bonus',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dd2a25de-fbe6-4511-a33c-befca7bc83aa'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dd2a25de-fbe6-4511-a33c-befca7bc83aa'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dd2a25de-fbe6-4511-a33c-befca7bc83aa'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stamp',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dd2a25de-fbe6-4511-a33c-befca7bc83aa'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='allowed_to_receive_stamps',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dd2a25de-fbe6-4511-a33c-befca7bc83aa'), primary_key=True, serialize=False),
        ),
    ]
