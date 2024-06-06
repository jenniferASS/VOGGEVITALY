# Generated by Django 5.0.6 on 2024-06-06 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roupas", "0004_alter_produto_genero_alter_produto_tamanho"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="produto",
            name="tamanho",
        ),
        migrations.AddField(
            model_name="categoria",
            name="foto_url",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="tamanho",
            name="nome",
            field=models.CharField(max_length=100),
        ),
    ]