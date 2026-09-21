"""Tes awal untuk memastikan kerangka pengujian benar-benar berjalan.

Berkas uji ditemukan Django karena namanya diawali "test" dan karena
direktori main/tests/ memiliki __init__.py. Menghapus __init__.py membuat
seluruh tes di dalamnya tidak pernah dijalankan.
"""

from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_returns_200(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_expected_template(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertTemplateUsed(response, "main/home.html")
