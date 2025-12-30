# USER BISA MASUKKAN DIA MAKAN APA. 
# KALORI DICATAT PERHARINYA. 
import csv
import os
from datetime import datetime
import pandas as pd

file_path = "List_kalori_per100gram.csv"

def cek(berat, kalori):
    if berat != kalori:
        return kalori
    
    elif berat == kalori:
        return "Tidak ada di database"
    
def catatan_harian(catatan_path, total_kalori):
    hari_ini = datetime.now()
    with open(catatan_path, 'w') as file:
        file.write(f"{hari_ini.date()}: {total_kalori} kalori\n")

def update_catatan(catatan_path, total_kalori):
    hari_ini = datetime.now()
    with open(catatan_path, 'a') as file:
        file.write(f"{hari_ini.date()}: {total_kalori} kalori\n")

def Isi_catatan(user):

    catatan_path = f"folder_catatan/catatan_harian_{user}.txt"

    print("=" * 50)
    print("LIST MAKANAN DIBAWAH INI UNTUK PENYAJIAN 100GRAM")
    print("=" * 50)
    database = pd.read_csv(file_path)
    print(database)
    print("=" * 50)
    
    # print("\nMakanan||Kalori per 100 gram")                         # DIMODIFIKASI PAKE PANDAS
    # with open(file_path, 'r') as file:                                # TETAP DISINI AJA BISI PANDASNYA ERROR
    #     filenya = csv.reader(file)
    #     for line in filenya:
    #         if 'Makanan' == line[0]: #biar headnya nggak ke print
    #             pass
    #         else:
    #             print(f"{line[0]}: {line[1]}")
                
    print("\nMakanan apa saja yang kamu makan? (ketik 'sudah' di input makanan jika kamu sudah selesai memasukkan list makanan kamu)\n")
    
    list_makanan_user = []
    list_berat_makanan = [] 
    copy_lbm = [] #copy dari list_berat_makanan

    while True:
        makanan_user = input("Makanan: ").lower()
        if makanan_user == 'sudah':
            break
        berat_makanan = float(input("Berat (gram): "))

        list_makanan_user.append(makanan_user)
        list_berat_makanan.append(berat_makanan)
        copy_lbm.append(berat_makanan)
    
    with open(file_path, 'r') as file: 
        datanya = csv.reader(file)
        for line in datanya: #mengubah file csv menjadi list-list per perbaris
            for i in range(len(list_makanan_user)): #membuat loop berdasarkan panjang list_makanan)user

                if list_makanan_user[i] == line[0]:                     #
                    line_float = float(line[1])                         #
                    kalori = (list_berat_makanan[i] / 100) * line_float #mengkonversi berat makanan menjadi kalori
                    list_berat_makanan[i] = kalori                      #
                    break 

    list_kalori = [] #untuk list kalori makanan yg ada kalorinya
    for i in range(len(list_makanan_user)):
        kalori = cek(berat=copy_lbm[i], kalori=list_berat_makanan[i])
        print(f"{list_makanan_user[i]} {copy_lbm[i]}(g): {kalori} kalori")

        if kalori != "Tidak ada di database":
            list_kalori.append(kalori)

    total_kalori = float(sum(list_kalori))
    print(f"Total Kalori: {total_kalori: .2f}\n")

    if os.path.exists(catatan_path):
        update_catatan(catatan_path, total_kalori)
    else:
        catatan_harian(catatan_path, total_kalori)

    print("Total kalori kamu sudah dimasukkan ke dalam catatan harian!")

def lihat_catatan(user): 
    catatan_path = f"folder_catatan/catatan_harian_{user}.txt"
    if os.path.exists(catatan_path):
        with open(catatan_path, 'r') as file:
            content = file.read()
        print(f"\n{content}\n")
    
    else:
        print("\nSepertinya kamu belum membuat catatan! Isi terlebih catatan kamu\n")

def menu(user):
    while True:
        print("1. Isi catatan")
        print("2. Lihat catatan")
        print("0. Kembali")
        pilih = input("Pilih 1, 2, atau 0: ")

        if pilih == '1':
            while True:
                Isi_catatan(user)
                yesOrNo = input("Apakah kamu sudah selesai mengisi catatan?\n-> ").lower()
                if yesOrNo in ['ya', 'yes', 'iya']:
                    break

        elif pilih == '2':
            lihat_catatan(user)

        elif pilih == '0':
            break
        
        else:
            print("Pilihan anda tidak valid! Silahkan masukkan angka 1, 2, atau 0")