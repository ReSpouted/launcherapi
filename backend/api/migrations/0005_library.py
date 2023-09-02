# Generated by Django 4.2.4 on 2023-09-02 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_file_projectbuild'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.CharField(max_length=128)),
                ('artifact_id', models.CharField(max_length=128)),
                ('version', models.CharField(max_length=128)),
                ('hash', models.CharField(max_length=32)),
                ('build', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_libraries', to='api.projectbuild')),
                ('mc_version', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mc_libraries', to='api.minecraft')),
            ],
        ),
    ]
