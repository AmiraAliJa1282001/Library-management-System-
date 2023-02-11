# Generated by Django 4.1.4 on 2023-02-10 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "library",
            "0005_remove_issuedbook_isbn_remove_issuedbook_student_id_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="issuedbook", name="book",),
        migrations.AddField(
            model_name="issuedbook",
            name="isbn",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="book",
                to="library.book",
            ),
        ),
    ]
