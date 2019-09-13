# Generated by Django 2.2.5 on 2019-09-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20190906_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musica',
            name='genero_musica',
        ),
        migrations.RemoveField(
            model_name='musica',
            name='link',
        ),
        migrations.AddField(
            model_name='musica',
            name='genero_musical',
            field=models.CharField(default=1, max_length=255, verbose_name='Genero musical'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musica',
            name='tempo_reproducao',
            field=models.CharField(default=1, max_length=50, verbose_name='Tempo de reprodução'),
            preserve_default=False,
        ),
    ]