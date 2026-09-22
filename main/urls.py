"""URLconf aplikasi main.

Tambahkan rute baru di dalam urlpatterns pada setiap drill. Selalu beri
argumen name agar rute dapat dipanggil lewat {% url %} dan reverse().
"""

from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("", views.show_main, name="show_main"),
    path("bookmarks/", views.show_bookmarks, name="show_bookmarks"),
    path("bookmarks/data/", views.bookmarks_data, name="bookmarks_data"),
    path("bookmarks/<uuid:pk>/archive/", views.toggle_archive, name="toggle_archive"),
    path("bookmarks/<uuid:pk>/delete/", views.delete_bookmark, name="delete_bookmark"),
]
