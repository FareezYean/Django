
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
from django.utils.html import escape

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def dictfetchone(cursor):
    """Mengubah satu hasil query menjadi dictionary."""
    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()

    if row is None:
        return None

    return dict(zip(columns, row))


def siswa_list(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, nama, umur, tgl_lahir, status_hadir, nilai_akhir
            FROM siswa
            ORDER BY id DESC
        """)
        data_siswa = dictfetchall(cursor)

    search_text = "Purworejo"

    return render(request, 'list.html', {
        'keyword': search_text,
        'data': data_siswa,
    })


def siswa_detail(request, id):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM siswa
            WHERE id = %s
            """,
            [id]
        )
        siswa = dictfetchone(cursor)    

    return render(request, 'detail.html', {
        'siswa': siswa,
    })


def siswa_create(request):
    # cek request yg masuk, klo dia POST (submit)
    if request.method == 'POST':        
        # kumpulkan data dari request post
        nama = request.POST.get('nama', '').strip()
        umur = request.POST.get('umur', '').strip()
        tgl_lahir = request.POST.get('tgl_lahir', '').strip()
        status_hadir = request.POST.get('status_hadir', '').strip()
        nilai_akhir = request.POST.get('nilai_akhir', '').strip()

        # eksekusi query insert ke tabel siswa
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO siswa (nama, umur, tgl_lahir, status_hadir, nilai_akhir)
                VALUES (%s, %s, %s, %s, %s)
                """,
                [nama, umur, tgl_lahir, status_hadir, nilai_akhir]
            )

        # klo berhasil maka redirect ke siswa list
        return redirect('siswa_list')

    # klo gk submit (GET)
    return render(request, 'form.html')


def siswa_update(request, id):
    # Ambil data siswa berdasarkan ID (SELECT)
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM siswa
            WHERE id = %s
            """,
            [id]
        )
        siswa = dictfetchone(cursor)
    
    # Jika siswa tidak ditemukan, redirect ke list
    if not siswa:
        return redirect('siswa_list')
    
    # Proses form jika ada submit POST
    if request.method == 'POST':
        nama = request.POST.get('nama', '').strip()
        umur = request.POST.get('umur', '').strip()
        tgl_lahir = request.POST.get('tgl_lahir', '').strip()
        status_hadir = request.POST.get('status_hadir', '').strip()
        nilai_akhir = request.POST.get('nilai_akhir', '').strip()
        
        # Eksekusi query UPDATE ke tabel siswa berdasarkan ID
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE siswa
                SET nama = %s, umur = %s, tgl_lahir = %s, status_hadir = %s, nilai_akhir = %s
                WHERE id = %s
                """,
                [nama, umur, tgl_lahir, status_hadir, nilai_akhir, id]
            )
        
        # Redirect ke detail siswa setelah berhasil update
        return redirect('siswa_detail', id=id)
    
    # Tampilkan form dengan data siswa yang sudah terisi (GET)
    return render(request, 'siswa_update.html', {
        'siswa': siswa,
    })


def siswa_delete(request, id):
    # Ambil data siswa berdasarkan ID (SELECT)
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM siswa
            WHERE id = %s
            """,
            [id]
        )
        siswa = dictfetchone(cursor)
    
    # Jika siswa tidak ditemukan, redirect ke list
    if not siswa:
        return redirect('siswa_list')
    
    # Proses delete jika ada submit POST
    if request.method == 'POST':
        # Eksekusi query DELETE dari tabel siswa berdasarkan ID
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM siswa
                WHERE id = %s
                """,
                [id]
            )
        
        # Redirect ke list siswa setelah berhasil delete
        return redirect('siswa_list')
    
    # Tampilkan halaman konfirmasi delete (GET)
    return render(request, 'siswa_delete.html', {
        'siswa': siswa,
    })


# Create your views here.
