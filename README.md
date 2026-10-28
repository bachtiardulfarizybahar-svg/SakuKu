SakuKu: Pencatat Keuangan Magang Berbasis CLI

1. Judul & Deskripsi

SakuKu adalah aplikasi berbasis antarmuka baris perintah (CLI) yang dibuat untuk membantu siswa mencatat dan mengelola aliran uang saku saat mereka menjalani Praktik Kerja Lapangan (PKL) atau magang.

Aplikasi ini dibuat karena anak magang sering kesulitan mengontrol pengeluaran harian. Dengan SakuKu, pengguna dapat mencatat pemasukan dan pengeluaran menurut kategori. Pengguna juga dapat melihat sisa saldo secara real‑time, menghapus transaksi yang salah, dan melihat rangkuman pengeluaran terbesar.

2. Teknologi yang Digunakan

- Bahasa Pemrograman: Python 3

- Modul bawaan Python: `json` untuk menyimpan data, `os` untuk membersihkan layar terminal, dan `datetime` untuk mencatat tanggal secara otomatis.

- Struktur data: List of Dictionary, yang memanajemen data transaksi di dalam memori.

3. Pemanfaatan AI (AI Usage Disclosure)

- Alat AI yang digunakan: Gemini

- Contoh prompt utama:

- Berikan kerangka fungsi Python untuk aplikasi pencatat keuangan berbasis CLI.

- Bagaimana cara memvalidasi input angka pada Python menggunakan try except agar program tidak error saat diisi huruf?

- Penyesuaian/perbaikan mandiri terhadap saran AI:

- Kami memodifikasi logika penghapusan data transaksi dari saran awal AI. Kami memakai loop enumerate agar pencarian ID transaksi asli tidak menimbulkan error IndexError.

- Kami menambahkan fungsi format_rupiah sendiri agar pemisah ribuan berubah dari koma menjadi titik, sesuai format Indonesia.

4. Panduan Penggunaan

A. Pastikan Python 3 sudah terpasang di komputer atau laptop.

B. Buka aplikasi Terminal atau Command Prompt.

C. Masuk ke direktori folder tempat file proyek disimpan.

D. Jalankan perintah berikut:

```bash

python main.py

```

5. Masukkan pilihan menu 1 sampai 5 sesuai kebutuhan pencatatan. Data transaksi akan tersimpan otomatis di berkas `uang_saku_magang.json`.

5. Identitas Pengembang

- Nama 1: Bachtiar Dul Farizy Bahar | Kelas: XI TKJ | Jurusan: Teknik Komputer dan Jaringan | Asal Sekolah: SMK Dwija Bhakti 1 Jombang.

- Nama 2: Dafinza Fahrial Putra | Kelas: XI TKJ | Jurusan: Teknik Komputer dan Jaringan | Asal Sekolah: SMK Dwija Bhakti 1 Jombang.