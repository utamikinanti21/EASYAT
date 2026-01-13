import json
import os

FILE_RESEP = "resep.json"

# =========================
# DATA HANDLING
# =========================

def load_resep():
    if not os.path.exists(FILE_RESEP):
        return []
    with open(FILE_RESEP, "r") as file:
        return json.load(file)

def save_resep(data):
    with open(FILE_RESEP, "w") as file:
        json.dump(data, file, indent=4)

# =========================
# FITUR RESEP
# =========================

def tampilkan_resep():
    resep = load_resep()
    if not resep:
        print("\nBelum ada resep makanan sehat.\n")
        return

    print("\n=== DAFTAR RESEP MAKANAN SEHAT ===")
    for i, r in enumerate(resep, start=1):
        print(f"{i}. {r['nama']} | {r['kalori']} kal")
    print()

def detail_resep():
    resep = load_resep()
    if not resep:
        print("\nBelum ada resep.\n")
        return

    tampilkan_resep()
    try:
        pilihan = int(input("Pilih nomor resep: ")) - 1
        r = resep[pilihan]

        print("\n--- DETAIL RESEP SEHAT ---")
        print("Nama Resep     :", r["nama"])
        print("Bahan          :", r["bahan"])
        print("Langkah        :", r["langkah"])
        print("Jumlah Kalori  :", r["kalori"])
        print("Informasi Gizi :", r["gizi"])
        print("Pembuat        :", r["pembuat"])
        print()
    except:
        print("Input tidak valid.\n")

def tambah_resep():
    print("\n=== TAMBAH RESEP MAKANAN SEHAT ===")
    nama = input("Nama resep          : ")
    bahan = input("Bahan               : ")
    langkah = input("Langkah pembuatan   : ")
    kalori = input("Jumlah kalori (kal) : ")
    gizi = input("Informasi gizi      : ")

    resep_baru = {
        "nama": nama,
        "bahan": bahan,
        "langkah": langkah,
        "kalori": kalori,
        "gizi": gizi,
        "pembuat": "Pengguna"
    }

    resep = load_resep()
    resep.append(resep_baru)
    save_resep(resep)

    print("\nResep berhasil ditambahkan!\n")

def cari_resep():
    resep = load_resep()
    if not resep:
        print("\nBelum ada resep makanan sehat.\n")
        return

    keyword = input("Masukkan kata kunci pencarian: ").lower()
    hasil = []

    for r in resep:
        if keyword in r['nama'].lower():
            hasil.append(r)

    if not hasil:
        print("\nTidak ada resep yang cocok dengan kata kunci tersebut.\n")
        return

    print(f"\n=== HASIL PENCARIAN RESEP ({len(hasil)} ditemukan) ===")
    for i, r in enumerate(hasil, start=1):
        print(f"{i}. {r['nama']} | {r['kalori']} kal")
    print()

    try:
        pilihan = int(input("Pilih nomor resep untuk melihat detail (atau 0 untuk kembali): ")) - 1
        if pilihan == -1:
            return
        r = hasil[pilihan]

        print("\n--- DETAIL RESEP SEHAT ---")
        print("Nama Resep     :", r["nama"])
        print("Bahan          :", r["bahan"])
        print("Langkah        :", r["langkah"])
        print("Jumlah Kalori  :", r["kalori"])
        print("Informasi Gizi :", r["gizi"])
        print("Pembuat        :", r["pembuat"])
        print()
    except:
        print("Input tidak valid.\n")

# =========================
# MENU UTAMA
# =========================

def menu():
    while True:
        print("===== DIET HELPER =====")
        print("1. Lihat Resep Makanan Sehat")
        print("2. Lihat Detail Resep")
        print("3. Cari Resep")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_resep()
        elif pilihan == "2":
            detail_resep()
        elif pilihan == "3":
            cari_resep()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan Diet Helper.")
            break
        else:
            print("Menu tidak tersedia.\n")

# =========================
# PROGRAM START
# =========================