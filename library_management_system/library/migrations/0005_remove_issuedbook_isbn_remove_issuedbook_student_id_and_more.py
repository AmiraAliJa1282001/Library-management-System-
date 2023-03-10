# Generated by Django 4.1.4 on 2023-02-10 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0004_alter_issuedbook_isbn_alter_issuedbook_student_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="issuedbook", name="isbn",),
        migrations.RemoveField(model_name="issuedbook", name="student_id",),
        migrations.AddField(
            model_name="issuedbook",
            name="book",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="book",
                to="library.book",
            ),
        ),
        migrations.AddField(
            model_name="issuedbook",
            name="student",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="student",
                to="library.student",
            ),
        ),
    ]
