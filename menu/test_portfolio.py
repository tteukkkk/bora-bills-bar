from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from unittest.mock import patch
import requests

class ApiFallbackTests(TestCase):
    @patch('menu.views.requests.get',side_effect=requests.Timeout)
    def test_apis_indisponiveis_nao_quebram_paginas(self,mock_get):
        for url in ['/cardapio/?busca=limonada','/curiosidade/','/']:
            with self.subTest(url=url):self.assertEqual(self.client.get(url).status_code,200)

    @patch('menu.views.requests.get')
    def test_lista_vazia_de_personagens(self,mock_get):
        mock_get.return_value.json.return_value={'items':[]}
        self.assertEqual(self.client.get('/curiosidade/').status_code,200)
