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
    profileUser = df.where(df['Username'] == username).dropna().reset_index(drop=True)
    print(profileUser)
    nama    = profileUser.loc[0,'Username']
    imt     = profileUser.loc[0,'IMT']
    berat   = profileUser.loc[0,'BeratBadan']
    tinggi  = profileUser.loc[0,'TinggiBadan']
    usia    = profileUser.loc[0,'Usia']
    sex     = profileUser.loc[0,'JenisKelamin']

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
            usia = int(input('Masukkan usia anda pada saat ini: '))
            imt, berat, tinggi = bmi.kalkulator_bmi()

            profileUser.loc[0,'IMT']         = imt
            profileUser.loc[0,'BeratBadan']  = berat
            profileUser.loc[0,'TinggiBadan'] = tinggi
            profileUser.loc[0,'Usia']        = usia

            print("Profile anda sudah berhasil di Update! Silahkan kembali ke Dashboard")