# Generated by Django 4.1.7 on 2023-04-24 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={},
        ),
        migrations.RemoveField(
            model_name="comment",
            name="active",
        ),
    ]
