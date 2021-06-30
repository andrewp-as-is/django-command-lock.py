# Generated by Django 3.1.7 on 2021-06-19 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('is_locked', models.BooleanField(default=True, verbose_name='locked')),
                ('pid', models.IntegerField()),
            ],
            options={
                'db_table': 'django_command_lock',
                'ordering': ('app', 'name'),
            },
        ),
        migrations.AddIndex(
            model_name='command',
            index=models.Index(fields=['app'], name='django_comm_app_320bf9_idx'),
        ),
        migrations.AddIndex(
            model_name='command',
            index=models.Index(fields=['name'], name='django_comm_name_634b96_idx'),
        ),
        migrations.AddIndex(
            model_name='command',
            index=models.Index(fields=['is_locked'], name='django_comm_is_lock_0ef5d8_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='command',
            unique_together={('app', 'name')},
        ),
    ]