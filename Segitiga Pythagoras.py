#login sederhana
nama = input("Masukan Nama : ")

while True :
    nim = input("Masukan NIM : ")
    if nim.isdigit():
        break
    else: 
        print("NIM harus berupa angka. Silahkan coba lagi")

kelas = input("Masukan Kelas : ")


print(f"Nama    : {nama}")
print(f"NIM     : {nim}")
print(f"Kelas   : SI {kelas} 2023")

#perhitungan rumus pythagoras

while True :
    hitung_sisi = input("Masukan Sisi yang mau dihitung (alas, tegak, miring) :")

    if hitung_sisi == "alas" :
        sisi_tegak = float(input("Masukan Sisi tegak : "))
        sisi_miring = float(input("Masukan Sisi miring : "))
        sisi_alas = (sisi_miring ** 2 - sisi_tegak ** 2) ** 0.5
        print(f"Hasil dari perhitungan tersebut menunjukkan bahwa sisi alasnya {sisi_alas}")
        break

    elif hitung_sisi == "tegak" :
        sisi_alas = float(input("Masukan Sisi alas : "))
        sisi_miring = float(input("Masukan Sisi miring : "))
        sisi_tegak = (sisi_miring ** 2 - sisi_alas ** 2) ** 0.5
        print(f"Hasil dari perhitungan tersebut menunjukkan bahwa sisi tegaknya {sisi_tegak}")
        break

    elif hitung_sisi == "miring" :
        sisi_alas = float(input("Masukan Sisi alas : "))
        sisi_tegak = float(input("Masukan Sisi tegak : "))
        sisi_miring = (sisi_alas ** 2 + sisi_tegak ** 2) ** 0.5
        print(f"Hasil dari perhitungan tersebut menunjukkan bahwa sisi miringnya {sisi_miring}")
        break

    else : 
        print("Masukan pilihan sisi yang benar (alas, tegak, miring). Silahkan coba masukan lagi")