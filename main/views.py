from django.shortcuts import render


def show_main(request):
    """Halaman beranda.

    Untuk sementara view ini hanya merender template tanpa data. Mulai
    drill mengenai kueri, beranda akan menampilkan satu data sorotan.
    """
    context = {}
    return render(request, "main/home.html", context)
