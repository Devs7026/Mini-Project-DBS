# Generated by Django 5.1.6 on 2025-03-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_alter_student_cgpa_alter_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('MIT', 'MIT'), ('MLS', 'MLS'), ('TAPMI', 'TAPMI'), ('DLHS', 'DLHS'), ('DOC', 'DOC'), ('SMIT', 'SMIT')], default='MIT', max_length=10),
        ),
    ]
