# bmi with python
def kalkulator_bmi():
    print("=== Kalkulator BMI ===")

    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (cm): "))

    if (berat <= 0) or (tinggi <= 0) : 
        print("Input Tidak valid. Berat dan tinggi harus lebih dari 0.")
        return

    tinggi_m = tinggi / 100
    bmi = berat / (tinggi_m ** 2)

    if bmi == 0 : 
        print()
        print("Input Tidak Valid.")

    elif bmi <= 16 : 
        kategori = "Kurus ekstrem (Severely Underweight)"
        metode = """
        Jika IMT anda berada di bawah 15, maka anda termasuk golongan Kurus Ekstrem (Severely underweight).
        Kondisi ini perlu perhatian khusus karena dapat berdampak pada kesehatan tubuh secara keseluruhan.
        Kami sangat menyarankan langkah-langkah berikut:
        1. Konsultasi dengan tenaga medis atau ahli gizi untuk mengetahui penyebab utama berat badan sangat rendah
        2. Tingkatkan asupan kalori secara bertahap dengan makanan bergizi dan seimbang
        3. Konsumsi makanan tinggi protein dan lemak sehat seperti telur, ikan, daging, alpukat, kacang-kacangan, susu full cream
        4. Makan dalam porsi kecil namun sering, sekitar 5–6 kali sehari
        5. Tambahkan camilan sehat bernutrisi tinggi seperti smoothie, yoghurt, keju, dan kacang
        6. Minum susu tinggi kalori atau suplemen nutrisi sesuai anjuran dokter
        7. Lakukan olahraga ringan untuk meningkatkan massa otot, hindari olahraga berat berlebihan
        8. Pastikan istirahat cukup dan kelola stres dengan baik
        9. Hindari merokok, alkohol, serta pola makan tidak teratur
        """
       

    elif 16 < bmi < 18.5:
        kategori = "Kurus (Underweight)"
        metode = """
            Jika IMT anda berkisar antara 15 - 18,5 maka anda termasuk golongan kurus (underweight),
            Kami sarankan untuk menambah berat badan yang sehat dengan cara:
            1. Makan dengan porsi sedikit namun sering, sekitar 5-6 kali sehari
            2. Makan makanan tinggi protein seperti telur, daging ayam, tempe, tahu dll
            3. Sering makan cemilan sehat seperti Sayur-sayuran, buah-buahan, salad atau kacang kacangan 
            4. Usahakan minum air 2L setiap hari, minum susu ataupun jus
            5. Olahraga teratur seperti bersepeda, jogging, senam dll
            6. Hindari untuk memakan junk food, merokok, dan minum alkohol
            7. Istirahat yang cukup dan kurangi stres
            """

    elif bmi < 25:
        kategori = "Normal (Healthy)"
        metode = """
            Jika IMT anda berkisar antara 18,5 sampai 24,9, ini adalah berat badan yang normal (healthy).
            Namun kami menyarankan untuk menjaga berat badan agar tetap normal dengan cara:
            1. Mengatur Pola makan seimbang (sehat dan bergizi)
            2. Usahakan minum air 2L setiap hari
            3. Melakukan Olahraga secara rutin 
            4. Hindari untuk memakan junk food, merokok, dan minum alkohol
            5. Istirahat yang cukup dan kurangi stres
            """

    elif bmi < 30:
        kategori = "Gemuk (Overweight)"
        metode = """
            Jika IMT anda berkisar antara 25 sampai 29,9, Maka anda termasuk golongan gemuk (overweight).
            Kami sarankan untuk menurunkan berat badan anda secara perlahan dengan cara:
            1. Defisit kalori sekitar 300-500 kalori setiap hari
            2. Kurangi karbo sederhana seperti gula, minuman manis, dan makanan olahan
            3. Tingkatkan protein (makan telur, daging ayam, tempe, tahu dll) dan serat (sayur dan buah)
            4. Usahakan minum air 2L setiap hari
            5. Melakukan Olahraga secara teratur, kombinasikan antara kardio dan latihan kekuatan otot 
            6. Hindari merokok, dan minum alkohol
            7. Istirahat yang cukup dan kurangi stres
            """
    else:
        kategori = "Obesitas (Obese)"
        metode = """
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
            """
     
    print("\nHasil perhitungan BMI kamu:")
    print("Nilai BMI:", round(bmi, 2))
    print("Kategori :", kategori)
    print("Metode diet yang direkomendasikan: ", metode)
        
    return bmi, berat, tinggi, metode

kalkulator_bmi()