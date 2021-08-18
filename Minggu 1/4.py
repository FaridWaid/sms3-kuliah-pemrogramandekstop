def maksimal(nilai):
    maks = 0
    for x in range(0,len(nilai)):
        if nilai[x] > maks:
            maks = nilai[x]
    return maks
def minimal(nilai):
    mini = 1000
    for x in range(0,len(nilai)):
        if nilai[x] < mini:
            mini = nilai[x]
    return mini

a=int(input("masukkan banyaknya nilai: "))
b = []
for x in range (a):
    c=int(input("masukkan nilainya = "))
    b.append(c)
print(b)

print("Nilai maksimal = ",maksimal(b))
print("Nilai minimal = ",minimal(b))
