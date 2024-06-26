# Generated by Django 5.0.6 on 2024-06-05 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roupas", "0003_alter_tamanho_nome"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="genero",
            field=models.CharField(
                choices=[
                    ("Feminino", "Feminino"),
                    ("Masculino", "Masculino"),
                    ("Unissex", "Unissex"),
                ],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="produto",
            name="tamanho",
            field=models.ManyToManyField(
                choices=[
                    ("PP", "PP"),
                    ("P", "P"),
                    ("M", "M"),
                    ("G", "G"),
                    ("GG", "GG"),
                    ("Extra GG", "Extra GG"),
                ],
                to="roupas.tamanho",
            ),
        ),
    ]
