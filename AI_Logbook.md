# AI LOGBOOK - KasKu (Pencatat Keuangan Magang)

Tim: Bachtiar Farizy & Dafinza Fahrial Putra | Sekolah: SMK Dwija Bhakti 1 Jombang

## Tahap 1: Eksplorasi Ide & Perancangan Solusi

- Alat AI: Gemini

- Prompt: Berikan 3 ide proyek aplikasi Python CLI untuk siswa SMK dengan tema solusi kehidupan sehari-hari.

- Ringkasan Jawaban AI: AI memberi tiga rekomendasi: aplikasi pencatat keuangan harian, sistem pengingat tugas (to-do list), dan kalkulator prediksi nilai. Semuanya bisa dibuat dengan konsep dasar perulangan dan dictionary.

- Validasi & Modifikasi Mandiri: Kami memilih ide pencatat keuangan karena sangat relevan dengan kebutuhan saat PKL—misalnya mengelola uang saku. Kami fokus pada fitur utama: catat transaksi dan lihat rekap saldo. Dengan demikian, proyek bisa selesai dalam waktu 8 hari tanpa terlalu rumit.

## Tahap 2: Penyusunan Kerangka Kode (Scaffolding)

- Alat AI: Gemini

- Prompt: Buatkan kerangka fungsi (scaffolding) Python untuk aplikasi pencatat keuangan berbasis CLI.

- Ringkasan Jawaban AI: AI sarankan pakai struktur list of dictionary dan beri kerangka fungsi kosong seperti `tambah_transaksi()`, `lihat_laporan()`, serta menu utama dengan `while True`.

- Validasi & Modifikasi Mandiri: Kami pakai struktur menu dari AI sebagai dasar, tapi kami tambahkan fungsi `muat_data()` dan `simpan_data()` pakai modul `json`. Tujuannya supaya data transaksi tetap tersimpan meskipun terminal ditutup. Ini sangat penting agar pengguna tidak kehilangan catatan keuangannya.

## Tahap 3: Pemecahan Masalah & Penanganan Galat (Debugging)

- Alat AI: Gemini

- Prompt: Kenapa program saya error ValueError saat kolom jumlah uang diisi dengan huruf, dan bagaimana cara mencegahnya?

- Ringkasan Jawaban AI: AI jelaskan bahwa `int()` tidak bisa mengubah teks jadi angka. Untuk hindari error, gunakan `try-except ValueError` di dalam perulangan agar program minta input ulang.

- Validasi & Modifikasi Mandiri: Kami terapkan solusi ini di fungsi `tambah_transaksi()`. Untuk pesan error-nya, kami ubah jadi lebih ramah pengguna, misalnya “Mohon masukkan angka saja, bukan huruf atau simbol.” Daripada nanti muncul pesan galat teknis yang membingungkan.

## Tahap 4: Refleksi & Penjelasan Kode

- Alat AI: Gemini

- Prompt: Tolong jelaskan cara kerja format `{jumlah:,}` pada bahasa Python.

- Ringkasan Jawaban AI: AI jelaskan bahwa tanda koma dalam f-string `{jumlah:,}` berfungsi untuk menambahkan pemisah ribuan otomatis pada angka, misalnya 1000000 jadi 1,000,000.

- Validasi & Modifikasi Mandiri* Setelah paham, kami terapkan fitur ini di fungsi `lihat_laporan()`. Kami juga sesuaikan spasi kolom tabel secara manual biar tampilan daftar transaksi rapi dan mudah dibaca di terminal. Ini penting agar pengguna tidak kesulitan melihat data keuangannya.