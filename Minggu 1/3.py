print("Program menghitung BMI(Body MAss Index")
BB = float(input("Masukkan berat badan anda((kg): "))
TB = float(input("Masukkan tinggi badan anda(m): "))
BMI = BB/(TB*TB)
print("BMI anda = ",BMI)
if BMI < 18.5:
    print("Berat badan kurang")
elif 18.5<=BMI<=22.9:
    print("Berat badan normal")
elif BMI>= 30:
    print("Obesitas")
