#Elemen Kompotisi I

print('@@@@ @@@      @@     @@    @')
print('@    @  @    @  @    @ @   @')
print('@@@@ @@@    @@@@@@   @  @  @')
print('@    @@    @      @  @   @ @')
print('@    @ @  @        @ @    @@')


teks = input("Masukkan sebuah string dengan 4 karakter (huruf kecil): ")

if len(teks) != 4 or not teks.islower():
    print("Input harus tepat 4 huruf kecil!")
else:
    kapital = ""  
    for huruf in teks:
        kode = ord(huruf)
        kapital += chr(kode - 32)
    print("Hasil kapitalisasi string tersebut adalah:", kapital)

#Elemen Kompotisi II

print('@@@@ @@@      @@     @@    @')
print('@    @  @    @  @    @ @   @')
print('@@@@ @@@    @@@@@@   @  @  @')
print('@    @@    @      @  @   @ @')
print('@    @ @  @        @ @    @@')

str1 = input("Masukkan string pertama : ")
str2 = input("Masukkan string kedua   : ")
str3 = input("Masukkan string ketiga  : ")

hasil = str1 + str2 + str3

print("Hasil penggabungan tiga string tersebut adalah:", hasil)


#Elemen Kopotisi III

print('@@@@ @@@      @@     @@    @')
print('@    @  @    @  @    @ @   @')
print('@@@@ @@@    @@@@@@   @  @  @')
print('@    @@    @      @  @   @ @')
print('@    @ @  @        @ @    @@')

kalimat = input("Masukkan sebuah kalimat: ")

karakter = input("Karakter yang ingin dihitung jumlahnya: ")


if len(karakter) != 1:
    print("Harap masukkan hanya 1 karakter!")
else:

    jumlah = kalimat.count(karakter)

    print(f"Jumlah karakter '{karakter}' dalam kalimat tersebut adalah: {jumlah}")


