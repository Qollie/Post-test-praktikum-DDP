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

#perhitungan rumus segitiga pythagoras

while True :
    hitung_sisi = input("Masukan Sisi yang mau dihitung (alas, tegak, miring) :")

    if hitung_sisi == "alas":
        while True:
            sisi_tegak = input("Masukan Sisi tegak: ")
            sisi_miring = input("Masukan Sisi miring: ")
            if sisi_tegak.isnumeric() and sisi_miring.isnumeric():
                sisi_tegak = float(sisi_tegak)
                sisi_miring = float(sisi_miring)
                sisi_alas = (sisi_miring ** 2 - sisi_tegak ** 2) ** 0.5
                print(f"Hasil dari perhitungan tersebut menunjukkan bahwa sisi alasnya {sisi_alas}")
                print(type(sisi_alas))
                break
            else:
                print("Panjang sisi harus berupa angka. Silakan coba lagi.")
        break

    elif hitung_sisi == "tegak" :
        while True:
            sisi_alas = (input("Masukan Sisi alas : "))
            sisi_miring = (input("Masukan Sisi miring : "))
            if sisi_alas.isnumeric() and sisi_miring.isnumeric():
                sisi_alas = float(sisi_alas)
                sisi_miring = float(sisi_miring)
                sisi_tegak = (sisi_miring ** 2 - sisi_alas ** 2) ** 0.5
                print(f"Hasil dari perhitungan tersebut menunjukkan bahwa sisi tegaknya {sisi_tegak}")
                break
            else:
                print("Panjang sisi harus berupa angka. Silakan coba lagi.")
        break

    elif hitung_sisi == "miring" :
        while True:
            sisi_alas = (input("Masukan Sisi alas : "))
            sisi_tegak = (input("Masukan Sisi tegak : "))
            if sisi_alas.isnumeric() and sisi_tegak.isnumeric():
                sisi_alas = float(sisi_alas)
                sisi_tegak = float(sisi_tegak)
                sisi_miring = (sisi_alas ** 2 + sisi_tegak ** 2) ** 0.5
                print(f"Hasil dari perhitungan tersebut menunjukkan bahwa sisi miringnya {sisi_miring}")
                break
            else:
                print("Panjang sisi harus berupa angka. Silakan coba lagi.")
        break
    
    else : 
        print("Masukan pilihan sisi yang benar (alas, tegak, miring). Silahkan coba masukan lagi")

