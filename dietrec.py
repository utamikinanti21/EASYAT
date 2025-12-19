# DIET RECOMENDATION PY 
def Pilihan_Metode():
    while True:
        print("Pilihan rekomendasi metode diet yang bisa dilakukan")
        print("1. Metode diet untuk IMT < 18,5")
        print("2. Metode diet untuk IMT 18,5 - 24,9")
        print("3. Metode diet untuk IMT 25 - 29,9")
        print("4. Metode diet untuk IMT >= 30")
        print("0. Balik ke menu awal")

        metode = input("Pilih dari 0-4: ")

        if metode == '1':
            print("""
            Jika IMT anda < 18,5 maka anda termasuk golongan kurus (underweight),
            Kami sarankan untuk menambah berat badan yang sehat dengan cara:
            1. Makan dengan porsi sedikit namun sering, sekitar 5-6 kali sehari
            2. Makan makanan tinggi protein seperti telur, daging ayam, tempe, tahu dll
            3. Sering makan cemilan sehat seperti Sayur-sayuran, buah-buahan, salad atau kacang kacangan 
            4. Usahakan minum air 2L setiap hari, minum susu ataupun jus
            5. Olahraga teratur seperti bersepeda, jogging, senam dll
            6. Hindari untuk memakan junk food, merokok, dan minum alkohol
            7. Istirahat yang cukup dan kurangi stres
            """)

        elif metode == '2':
            print("""
            Jika IMT anda berkisar antara 18,5 sampai 24,9, ini adalah berat badan yang normal (healthy).
            Namun kami menyarankan untuk menjaga berat badan agar tetap normal dengan cara:
            1. Mengatur Pola makan seimbang (sehat dan bergizi)
            2. Usahakan minum air 2L setiap hari
            3. Melakukan Olahraga secara rutin 
            4. Hindari untuk memakan junk food, merokok, dan minum alkohol
            5. Istirahat yang cukup dan kurangi stres
            """)

        elif metode == '3':
            print("""
            Jika IMT anda berkisar antara 25 sampai 29,9, Maka anda termasuk golongan gemuk (overweight).
            Kami sarankan untuk menurunkan berat badan anda secara perlahan dengan cara:
            1. Defisit kalori sekitar 300-500 kalori setiap hari
            2. Kurangi karbo sederhana seperti gula, minuman manis, dan makanan olahan
            3. Tingkatkan protein (makan telur, daging ayam, tempe, tahu dll) dan serat (sayur dan buah)
            4. Usahakan minum air 2L setiap hari
            5. Melakukan Olahraga secara teratur, kombinasikan antara kardio dan latihan kekuatan otot 
            6. Hindari merokok, dan minum alkohol
            7. Istirahat yang cukup dan kurangi stres
            """)

        elif metode == '4':
            print("""
            Jika IMT anda 30 atau lebih Maka anda termasuk golongan obesitas. 
            Kami sarankan menghubungi dokter ahli sambil menurunkan berat badan 
            1. Defisit kalori sekitar 500 kalori
            2. Kurangi minuman manis dan makanan olahan yang mengandung lemak dan gula tinggi
            3. Pilih makanan yang berprotein namun rendah lemak (seperti ikan atau daging ayam)
            4. Perbanyak konsumsi serat seperti buah, sayuran dan biji-bijian      
            5. Usahakan minum air 2L/hari
            6. Melakukan Olahraga minimal 150 menit/minggu (sekitar 30 menit x 5hari) , 
            7. Mengkombinasikan antara kardio dan latihan kekuatan otot 
            8. Hindari merokok, dan minum alkohol
            9. Istirahat yang cukup dan kurangi stres
            """)
            
        elif metode == '0':
            break
        else:
            print("\nInvalid! Silahkan memasukkan angka dari 0-4\n")
