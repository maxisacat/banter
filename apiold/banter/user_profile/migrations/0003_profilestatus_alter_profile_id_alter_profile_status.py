# Generated by Django 4.2.5 on 2023-09-26 17:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_remove_profile_hashed_password_profile_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='user_profile.profilestatus'),
        ),
    ]
