import csv
import dietrec as dr
import bmi

file_path = 'data_Akun.csv'

def signup(username, password): 
    with open(file_path, 'r') as file:
        membaca_data = csv.reader(file)
        hasil = True
        for i in membaca_data:  #diubah menjadi list
            if len(i) == 0: #cek agar tidak ada index error
                pass
            elif username in i[0]:
                print("Maaf, username ini sudah terpakai. Silahkan buat username yang berbeda")
                hasil = False

    if hasil:
        with open(file_path, 'a') as file:
            menambah_data = csv.DictWriter(file, fieldnames=['Username', 'Password'])
            menambah_data.writerow({
                'Username': username,
                'Password': password
            })

        print("Akun anda berhasil dibuat!")
        return hasil
    
def login(username, password):
    with open(file_path, 'r') as file:
        membaca_data = csv.reader(file)
        hasil = False

        for i in membaca_data: #diubah menjadi list
            if len(i) == 0: #cek agar tidak ada index error
                pass
            elif (username == i[0]) and (password == i[1]):
                hasil = True
            if hasil:
                break

        return hasil
    
def dashboard(username):
    print(f"\nSelamat datang {username}")
    print('-' * 21)
    print('| ','Easy@ Dashboard', ' |')
    print('-' * 21)

    while True:
        print("Menu: ")
        print("1. Hitung BMI (Body Mass Index)")
        print("2. Rekomendasi Diet")
        print("3. Resep-resep")
        print("4. Calory Tracking")
        print("5. Profile User") # optional
        print("0. Keluar")

        menu = int(input("Pilih dari 0-5: "))

        if menu == '0':
            print("\nSelamat Tinggal! Semoga Harimu Menyenangkan! ^_^ ")
            break
        elif menu == '1':
            bmi.kalkulator_bmi() # file bmi.py
        elif menu == '2':
            dr.Pilihan_Metode()# file dietrec.py
        elif menu == '3':
            pass # file reseppage.py
        elif menu == '4':
            pass # file calorytrack.py
        elif menu == '5': #optional
            pass # optional
        else:
            print("\nInvalid! Silahkan memasukkan angka dari 0-5\n")
    
def signup_login():
    print("Selamat Datang di Easy@!: ")
    print('-' * 11)
    print('| ','Easy@', ' |')
    print('-' * 11)

    while True:
        print("1. Sign-up")
        print("2. Login")
        print("0. Keluar")

        pilihan = input("Pilih 1, 2, atau 0: ")

        if pilihan == '1':
            while True:
                username_input = input("Buat Username: ")
                password_input = input("Buat Password: ")
                cek_hasil = signup(username_input, password_input)

                if cek_hasil:
                    break

        elif pilihan == '2':
            num = 0
            while num != 3:
                username_input = input("Username: ")
                password_input = input("Password: ")
                cek_login = login(username_input, password_input)
                if cek_login:
                    user = username_input
                    break
                else:
                    print("Username atau password kamu salah, silahkan masukkan kembali!")
                    num += 1
            if num == 3:
                print("Kamu salah Username atau Password 3 kali, jika kamu belum memiliki akun \nSilahkan Sign-up terlebih dahulu")
            if cek_login:
                dashboard(user)
                break
                    
        elif pilihan == '3':
            print("Selamat Tinggal! Semoga Harimu Menyenangkan! ^_^ ")
            break
        else:
            print("Invalid! \nDimohon untuk memasukkan angka 1, 2 atau 3")

signup_login()
