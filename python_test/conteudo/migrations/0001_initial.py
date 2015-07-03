# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('slug', autoslug.fields.AutoSlugField(populate_from='nome', verbose_name='Slug', editable=False)),
                ('pais', models.CharField(max_length=30, verbose_name='Pa\xeds de Origem')),
                ('foto', models.ImageField(upload_to='atores/', verbose_name='Foto')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('slug', autoslug.fields.AutoSlugField(populate_from='nome', verbose_name='Slug', editable=False)),
                ('sinopse', models.TextField(verbose_name='Sinopse')),
                ('cartaz', models.ImageField(upload_to='cartazes/', verbose_name='Cartaz')),
                ('atores', models.ManyToManyField(to='conteudo.Ator')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('slug', autoslug.fields.AutoSlugField(populate_from='nome', verbose_name='Slug', editable=False)),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='filme',
            name='generos',
            field=models.ManyToManyField(to='conteudo.Genero'),
            preserve_default=True,
        ),
    ]
