# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from autoslug import AutoSlugField


class Ator(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    slug = AutoSlugField(verbose_name='Slug', populate_from='nome')

    pais = models.CharField(verbose_name='País de Origem', max_length=30)
    foto = models.ImageField(verbose_name='Foto', upload_to='atores/')

    def __unicode__(self):
        return '{}'.format(self.nome)

    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'nome__icontains')

    def get_absolute_url(self):
        return reverse('conteudo:ator', args=(self.slug,))

    class Meta:
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'
        ordering = ('nome',)


class Filme(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    slug = AutoSlugField(verbose_name='Slug', populate_from='nome')

    sinopse = models.TextField(verbose_name='Sinopse')
    cartaz = models.ImageField(verbose_name='Cartaz', upload_to='cartazes/')

    atores = models.ManyToManyField('Ator')
    generos = models.ManyToManyField('Genero')

    def __unicode__(self):
        return '{}'.format(self.nome)

    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'nome__icontains')

    def get_absolute_url(self):
        return reverse('conteudo:filme', args=(self.slug,))

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ('nome',)


class Genero(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    slug = AutoSlugField(verbose_name='Slug', populate_from='nome')

    def __unicode__(self):
        return '{}'.format(self.nome)

    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'nome__icontains')

    def get_absolute_url(self):
        return reverse('conteudo:genero', args=(self.slug,))

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        ordering = ('nome',)
