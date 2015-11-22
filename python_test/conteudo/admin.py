# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Ator, Genero, Filme


@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    pass


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    raw_id_fields = ('atores', 'generos')


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass
