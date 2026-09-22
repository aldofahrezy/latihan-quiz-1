from django.core import serializers
from django.db.models.aggregates import Max
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_GET
from main.forms import BookmarkForm
from main.models import Bookmark


def show_main(request):
    """Halaman beranda.

    Untuk sementara view ini hanya merender template tanpa data. Mulai
    drill mengenai kueri, beranda akan menampilkan satu data sorotan.
    """
    context = {}
    return render(request, "main/home.html", context)

def show_bookmarks(request):
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:show_bookmarks")
    else:
        form = BookmarkForm()
    context = {"form": form, "bookmarks": Bookmark.objects.all()}
    return render(request, "bookmarks.html", context)

@require_POST
def toggle_archive(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    bookmark.is_archived = not bookmark.is_archived
    bookmark.save(update_fields=["is_archived"])
    return redirect("main:show_bookmarks")

@require_POST
def delete_bookmark(request, pk):
    get_object_or_404(Bookmark, pk=pk).delete()
    return redirect("main:show_bookmarks")

def show_home(request):
    active = Bookmark.object.filter(is_archived=False)

    top_priority = active.aggregate(Max("priority"))["priority__max"]
    if top_priority:
        candidates = active.filter(priority=top_priority)
    else:
        candidates = active

    featured = candidates.order_by("?").first()

    return render(request, "home.html", {"featured": featured})

@require_GET
def bookmarks_data(request):
    CONTENT_TYPES = {"json": "application/json", "xml": "application/xml"}

    fmt = request.GET.get("format", "json")
    if fmt not in CONTENT_TYPES:
        return HttpResponseBadRequest("Format tidak didukung")

    bookmarks = Bookmark.objects.all()

    archived = request.GET.get("archived")
    if archived in {"true", "false"}:
        bookmarks = bookmarks.filter(is_archived=(archived=="true"))

    payload = serializers.serialize(fmt, bookmarks)
    return HttpResponse(payload, content_type=CONTENT_TYPES[fmt])
    