# Generated by Django 4.1.4 on 2023-02-10 22:55

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0008_remove_issuedbook_book_issuedbook_isbn_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="IssuedBooks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("student_id", models.CharField(blank=True, max_length=100)),
                ("isbn", models.CharField(max_length=13)),
                ("issued_date", models.DateField(auto_now=True)),
                ("expiry_date", models.DateField(default=library.models.expiry)),
            ],
        ),
        migrations.DeleteModel(name="IssuedBook",),
    ]
