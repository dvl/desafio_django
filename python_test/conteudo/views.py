# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models import Count, Q
from django.views import generic

from .models import Ator, Genero, Filme


class AtorDetailView(generic.DetailView):
    model = Ator


class FilmeDetailView(generic.DetailView):
    model = Filme

    def get_queryset(self):
        return (
            super(FilmeDetailView, self).get_queryset()
            .prefetch_related('generos')
            .prefetch_related('atores')
        )

    def get_filmes_relacionados(self):
        return (
            self.model.objects
            .exclude(pk=self.object.pk)
            .filter(
                Q(atores__in=self.object.atores.all()) |
                Q(generos__in=self.object.generos.all())
            )
            .annotate(peso=Count('pk'))
            .order_by('-peso')
        )[:10]

    def get_context_data(self, **kwargs):
        context = super(FilmeDetailView, self).get_context_data(**kwargs)
        context.update({
            'filmes_relacionados': self.get_filmes_relacionados()
        })

        return context


class FilmeListView(generic.ListView):
    model = Filme

    def get(self, request, *args, **kwargs):
        self.genero = None
        slug = self.kwargs.get('slug')

        if slug:
            self.genero = Genero.objects.get(slug=slug)

        return super(FilmeListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(FilmeListView, self).get_queryset()

        ordem = self.request.GET.get('ordem')
        if ordem and ordem == 'desc':
            qs = qs.order_by('-nome')

        if self.genero:
            qs = qs.filter(generos=self.genero)

        return qs

    def get_context_data(self, **kwargs):
        context = super(FilmeListView, self).get_context_data(**kwargs)
        context.update({
            'genero': self.genero,
        })

        return context
