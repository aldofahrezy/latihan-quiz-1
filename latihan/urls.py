"""URLconf tingkat proyek.

Seluruh rute aplikasi didelegasikan ke main/urls.py memakai include(),
sehingga berkas ini hampir tidak pernah perlu diubah selama latihan.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
]
