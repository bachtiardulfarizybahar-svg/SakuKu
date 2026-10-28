import json
import os
from datetime import datetime

BERKAS_DATA = "uang_saku_magang.json"

# fungsi untuk membersihkan layar terminal
def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

# fungsi memformat angka ke rupiah (contoh: Rp15.000)
def format_rupiah(angka):
    return f"Rp{angka:,.0f}".replace(",", ".")

# membaca data dari file JSON
def muat_data():
    if os.path.exists(BERKAS_DATA):
        try:
            with open(BERKAS_DATA, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

# menyimpan data list ke file JSON
def simpan_data(data):
    with open(BERKAS_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# validasi input angka agar tidak error saat dimasukkan huruf
def minta_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            if angka <= 0:
                print("jumlahnya harus lebih dari 0, coba lagi yaa")
                continue
            return angka
        except ValueError:
            print("masukkan berupa angka bulat saja")

# fungsi mencatat transaksi baru
def tambah_transaksi(data, jenis):
    bersihkan_layar()
    print(f"=== Tambah Data {jenis} ===")
    
    kategori = "-"
    if jenis == "Pengeluaran":
        print("\npilih kategori pengeluaran:")
        print("1. makan dan Minum")
        print("2. transportasi")
        print("3. kebutuhan tugas/pint")
        print("4. lainnya")
        
        kategori_list = ["makan/minum", "transportasi", "tugas/print", "lainnya"]
        while True:
            pil = input("pilihan kategori (1-4): ")
            if pil in ["1", "2", "3", "4"]:
                kategori = kategori_list[int(pil) - 1]
                break
            print("pilihan kamu tidak ada yaa, masukkan angka 1 sampai 4")

    keterangan = input("keterangan transaksi: ")
    jumlah = minta_angka("jumlah nominal (Rp): ")
    
    # generate id unik berdasarkan data terakhir
    id_baru = 1 if not data else max(t["id"] for t in data) + 1
            
    transaksi_baru = {
        "id": id_baru,
        "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "jenis": jenis,
        "kategori": kategori,
        "keterangan": keterangan,
        "jumlah": jumlah
    }
    
    data.append(transaksi_baru)
    simpan_data(data)
    print(f"\nData {jenis.lower()} berhasil disimpann!")
    input("tekan Enternya untuk kembali ke menu...")

# menghapus transaksi berdasarkan id
def hapus_transaksi(data):
    bersihkan_layar()
    print("=== hapus transaksi ===")
    if not data:
        print("belum ada data transaksi yang tersimpan -_-")
        input("\ntekan Enter untuk kembali...")
        return

    # tampilkan 5 data transaksi terakhir
    print("5 Transaksi Terakhir:")
    for t in data[-5:]:
        print(f"ID: {t['id']} | {t['tanggal']} | {t['jenis']} | {t['keterangan']} | {format_rupiah(t['jumlah'])}")
    
    print("-" * 50)
    id_hapus = minta_angka("masukkan id transaksi yang akan dihapus (0 untuk batal yaa): ")
    
    if id_hapus == 0:
        return
        
    for i, t in enumerate(data):
        if t["id"] == id_hapus:
            data.pop(i)
            simpan_data(data)
            print(f"data transaksi id {id_hapus} berhasil dihapus")
            input("\ntekan Enter untuk kembali...")
            return
            
    print(f"transaksi dengan id {id_hapus} tidak ditemukan, huemm...")
    input("\ntekan Enter untuk kembali...")

# tampilan laporan keuangan lengkap
def lihat_laporan(data):
    bersihkan_layar()
    if not data:
        print("=== laporan keuangan ===")
        print("belum ada catatan transaksi nii")
        input("\ntekan Enter untuk kembali...")
        return
        
    print("=" * 70)
    print(f"{'ID':<4} | {'TANGGAL':<16} | {'JENIS':<12} | {'KATEGORI':<12} | {'KETERANGAN':<14} | JUMLAH")
    print("=" * 70)
    
    saldo = 0
    rekap_kategori = {}

    for t in data:
        if t["jenis"] == "Pemasukan":
            saldo += t["jumlah"]
        else:
            saldo -= t["jumlah"]
            kat = t["kategori"]
            rekap_kategori[kat] = rekap_kategori.get(kat, 0) + t["jumlah"]
            
        print(f"{t['id']:<4} | {t['tanggal']:<16} | {t['jenis']:<12} | {t['kategori']:<12} | {t['keterangan'][:14]:<14} | {format_rupiah(t['jumlah'])}")
        
    print("=" * 70)
    print(f"SISA SALDO UANG SAKU: {format_rupiah(saldo)}")
    print("=" * 70)
    
    if rekap_kategori:
        print("\nringkasan Pengeluaran perkategori:")
        kategori_boros = ""
        max_pengeluaran = 0
        
        for kat, total in rekap_kategori.items():
            print(f"- {kat}: {format_rupiah(total)}")
            if total > max_pengeluaran:
                max_pengeluaran = total
                kategori_boros = kat
                
        print(f"\ncatatan buat kamu: pengeluaran terbanyak ada pada kategori '{kategori_boros}'. Jadi hemat hemat yaa kalau di '{kategori_boros}'.")

    input("\ntekan Enter untuk kembali ke menu...")

# loop menu utama
def main():
    data_transaksi = muat_data()
    
    while True:
        bersihkan_layar()
        print("===================================")
        print(" SAKUKU - PENCATAT UANG MAGANG :p- ")
        print("===================================")
        print("1. catat pemasukan / uang saku")
        print("2. catat pengeluaran")
        print("3. lihat laporan keuangan")
        print("4. hapus transaksi")
        print("5. keluar")
        print("===================================")
        
        pilihan = input("pilih menu (1-5): ")
        
        if pilihan == "1":
            tambah_transaksi(data_transaksi, "Pemasukan")
        elif pilihan == "2":
            tambah_transaksi(data_transaksi, "Pengeluaran")
        elif pilihan == "3":
            lihat_laporan(data_transaksi)
        elif pilihan == "4":
            hapus_transaksi(data_transaksi)
        elif pilihan == "5":
            bersihkan_layar()
            print("program selesai, terima kasih\n")
            break
        else:
            print("pilihan tidak valid, tekan Enter untuk mengulang")
            input()

if __name__ == "__main__":
    main()
