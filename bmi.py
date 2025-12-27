# bmi with python
print("=== Kalkulator BMI ===")

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))

tinggi_m = tinggi / 100

bmi = berat / (tinggi_m ** 2)

if bmi < 18.5:
    kategori = "Kurus (Underweight)"
elif bmi < 25:
    kategori = "Normal (Healthy)"
elif bmi < 30:
    kategori = "Gemuk (Overweight)"
else:
    kategori = "Obesitas (Obese)"

print("\nHasil perhitungan BMI kamu:")
print("Nilai BMI:", round(bmi, 2))
print("Kategori :", kategori)
