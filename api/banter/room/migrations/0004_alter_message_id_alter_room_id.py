# Generated by Django 4.2.5 on 2023-10-03 16:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_alter_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]