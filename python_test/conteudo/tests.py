# -*- coding: utf-8 -*-

from django.test import TestCase
from django.template import Context, Template

from model_mommy import mommy

from .models import Ator, Filme, Genero


class TestTemplateFilter(TestCase):
    TEMPLATE = Template('{% load pretty_join %} {{ object_list|pretty_join }}')

    def test_lista_com_um_item(self):
        gen = mommy.make(Genero)
        rendered = self.TEMPLATE.render(Context({'object_list': [gen]}))

        self.assertHTMLEqual(rendered, '<a href="{}">{}</a>'.format(
            gen.get_absolute_url(),
            gen.nome
        ))

    def test_lista_com_varios_items(self):
        gen = mommy.make(Genero, _quantity=3)
        rendered = self.TEMPLATE.render(Context({'object_list': gen}))

        output = '''
            <a href="{}">{}</a>, <a href="{}">{}</a> e <a href="{}">{}</a>
        '''.format(
            gen[0].get_absolute_url(), gen[0].nome,
            gen[1].get_absolute_url(), gen[1].nome,
            gen[2].get_absolute_url(), gen[2].nome,
        )

        self.assertHTMLEqual(rendered, output)

    def test_objeto_sem_url(self):
        delattr(Genero, 'get_absolute_url')
        gen = mommy.make(Genero)
        rendered = self.TEMPLATE.render(Context({'object_list': [gen]}))

        self.assertHTMLEqual(rendered, '{}'.format(gen.nome))



class TestFilmeListView(TestCase):
    def test_todos_os_items_sao_exibidos_na_pagina_inicial(self):
        mommy.make(Filme, _quantity=30)
        response = self.client.get('/')

        self.assertEqual(len(response.context['object_list']), 30)

    def test_cabecalho_e_montado_corretamente(self):
        response = self.client.get('/')

        self.assertInHTML('<h1 class="fl">Listagem de Filmes</h1>', response.rendered_content)

    def test_ordenacao_e_respeitada(self):
        a = mommy.make(Filme, nome='AAA')
        b = mommy.make(Filme, nome='BBB')
        c = mommy.make(Filme, nome='CCC')

        response = self.client.get('/')
        self.assertListEqual(list(response.context['object_list']), [a, b, c])

        response = self.client.get('/?ordem=desc')
        self.assertListEqual(list(response.context['object_list']), [c, b, a])

    def test_genero_e_respeitado(self):
        gen1 = mommy.make(Genero, nome='gen1')
        gen2 = mommy.make(Genero, nome='gen2')

        mommy.make(Filme, generos=[gen1])
        mommy.make(Filme, generos=[gen2])
        mommy.make(Filme, generos=[gen1, gen2])

        response = self.client.get('/genero/gen1/')
        self.assertEqual(len(response.context['object_list']), 2)

        response = self.client.get('/genero/gen2/')
        self.assertEqual(len(response.context['object_list']), 2)
