"""URLconf aplikasi main.

Tambahkan rute baru di dalam urlpatterns pada setiap drill. Selalu beri
argumen name agar rute dapat dipanggil lewat {% url %} dan reverse().
"""

from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("", views.show_main, name="show_main"),
]
