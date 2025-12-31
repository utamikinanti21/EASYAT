import pandas as pd
import bmi

file_path = 'data_profile.csv'
def create_profile(username):
    print("\n======= Create Profile =======")
    usia = int(input("Silahkan masukkan usia anda: "))
    while True:
        print("\nSilahkan pilih jenis kelamin anda: ")
        print("1. Laki-laki")
        print("2. Perempuan")
        jenis = input("-> ")
        if jenis == '1':
            jenisKelamin = "Laki-laki"
            break
        elif jenis == '2':
            jenisKelamin = "Perempuan"
            break
        else:
            print("\nSilahkan masukkan angka 1 atau 2!")
    imt, beratBdn, tinggiBdn = bmi.kalkulator_bmi()
    data = {
        'Username'      : [username], #dilist biar tidak ada value error
        'IMT'           : [imt],
        'BeratBadan'    : [beratBdn],
        'TinggiBadan'   : [tinggiBdn],
        'Usia'          : [usia],
        'JenisKelamin'  : [jenisKelamin]
    }

    df = pd.DataFrame(data)
    df.to_csv(file_path, mode= 'a', index=False, header=False)

    print("Profil anda berhasil dibuat! Silahkan kembali ke Dashboard")
    print("======= Create Profile =======\n")

def cek(username):
    df = pd.read_csv(file_path)
    df = df['Username']
    for i in df:
        if i == username:
            return True
    return False

def profile(username):
    df = pd.read_csv(file_path)
    nama   = df.loc[df['Username'] == username,'Username']
    imt    = df.loc[df['Username'] == username,'IMT']
    berat  = df.loc[df['Username'] == username,'BeratBadan']
    tinggi = df.loc[df['Username'] == username,'TinggiBadan']
    usia   = df.loc[df['Username'] == username,'Usia']
    sex    = df.loc[df['Username'] == username,'JenisKelamin']

    nama  : str   = nama.iloc[0]
    imt   : float = imt.iloc[0]
    berat : float = berat.iloc[0]
    tinggi: float = tinggi.iloc[0]
    usia  : int   = usia.iloc[0]
    sex   : str   = sex.iloc[0]

    print("\n======= Profile =======")
    print(f"""Username     : {nama}
IMT          : {imt}
Berat Badan  : {berat}
Tinggi Badan : {tinggi}
Usia         : {usia}
Jenis Kelamin: {sex}""")
    print("======= Profile =======\n")
    while True:
        print("1. Update Profile")
        print("0. Kembali")
        menu = input("-> ")
        if menu == '0':
            break

        elif menu == '1':
            usia_baru = int(input('Masukkan usia anda pada saat ini: '))
            imt_baru, berat_baru, tinggi_baru = bmi.kalkulator_bmi()
            df.loc[df['Username'] == username, 'IMT']        = imt_baru
            df.loc[df['Username'] == username,'BeratBadan']  = berat_baru
            df.loc[df['Username'] == username,'TinggiBadan'] = tinggi_baru
            df.loc[df['Username'] == username,'Usia']        = usia_baru

            df.to_csv(file_path, index=False)

            print("Profile anda sudah berhasil di Update! Anda akan kembali ke Dashboard")
        else:
            print("Silahkan masukkan angka 1 atau 0!")