# Proyek Latihan Django

Titik awal untuk seluruh drill pada dokumen *Pengembangan Web dengan Django*
(Pemrograman Berbasis Platform). Proyek ini sengaja dibuat kosong: kerangkanya
sudah berjalan, tetapi belum ada model, form, maupun halaman data. Setiap drill
menambahkan satu lapisan di atasnya.

## Menjalankan proyek

```bash
git clone <url-repositori-ini> latihan-django
cd latihan-django

python -m venv env
source env/bin/activate        # macOS atau Linux
env\Scripts\activate           # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Buka <http://127.0.0.1:8000/>. Jika halaman beranda tampil, lingkungan Anda
sudah siap dan Anda dapat mulai dari Drill 1.

## Isi kerangka

```
latihan/settings.py          aplikasi main, direktori templates, dan static sudah terdaftar
latihan/urls.py              mendelegasikan seluruh rute ke main/urls.py
main/urls.py                 baru berisi rute beranda bernama show_main
main/views.py                baru berisi show_main
main/models.py               kosong, diisi mulai Drill 1
main/forms.py                kosong, diisi mulai Drill 4
main/tests/test_smoke.py     dua tes contoh agar kerangka pengujian terbukti berjalan
templates/base.html          kerangka HTML dengan blok title, nav, content, dan footer
main/templates/main/home.html  halaman beranda yang mewarisi base.html
static/css/style.css         gaya seperlunya, termasuk kelas untuk daftar dan tombol aksi
```

## Peta drill

| Drill | Lapisan yang ditambahkan | Berkas utama |
| :--- | :--- | :--- |
| 1 | Model dan migrasi | `main/models.py`, `main/migrations/` |
| 2 | Rute bernama | `main/urls.py` |
| 3 | View POST, penolakan method, redirect | `main/views.py` |
| 4 | ModelForm, validasi, CSRF | `main/forms.py`, `main/views.py` |
| 5 | Template daftar dan keadaan kosong | `main/templates/main/` |
| 6 | Kueri, data sorotan, edge case | `main/views.py` |
| 7 | Endpoint serialisasi JSON dan XML | `main/views.py`, `main/urls.py` |
| 8 | Pengujian dan cakupan | `main/tests/` |
| 9 | Perapian kualitas kode | seluruh berkas |

## Perintah yang sering dipakai

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell
python manage.py test

coverage run manage.py test
coverage report

ruff check
ruff check --fix
```

Berkas `.coveragerc` sudah mengecualikan `env/`, migrasi, dan berkas konfigurasi
dari pengukuran, sehingga angka cakupan mencerminkan kode yang benar-benar Anda
tulis.

## Catatan

`SECRET_KEY` dibaca dari variabel lingkungan `DJANGO_SECRET_KEY` dengan nilai
cadangan yang jelas tidak aman. Nilai cadangan tersebut memadai untuk latihan di
mesin sendiri, tetapi harus diganti sebelum proyek dijalankan di tempat lain.
Pola ini juga alasan mengapa kunci asli tidak pernah ikut masuk ke repositori.
