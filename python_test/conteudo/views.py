# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views import generic

from .models import Ator, Genero, Filme


class AtorDetailView(generic.DetailView):
    model = Ator


class FilmeDetailView(generic.DetailView):
    model = Filme


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
