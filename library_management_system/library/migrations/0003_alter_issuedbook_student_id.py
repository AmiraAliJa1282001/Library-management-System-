# Generated by Django 4.1.4 on 2023-02-10 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_alter_issuedbook_student_id_alter_student_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issuedbook",
            name="student_id",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]