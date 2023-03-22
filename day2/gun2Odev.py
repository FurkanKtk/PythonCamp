ogrenciler = ["Furkan Kütük", "Engin Demiroğ", "Halit Kalaycı"]
print(ogrenciler)

#Aldığı isim soy isim ile listeye öğrenci ekleyen
def ogrenciEkle():
    isimSoyisim = input("Eklemek istediğiniz isim soyismi giriniz : ")
    ogrenciler.append(isimSoyisim)
    print(ogrenciler)


#Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
def ogrenciSilme():
    removeOgrenci = input("silmek istediğiniz öğrenciyi yazınız")
    print(ogrenciler)

#Listeye birden fazla öğrenci eklemeyi mümkün kılan
def ogrencilerEkle():
    x = int(input("Kaç ogrenci ismi gireceksiniz:"))
    for i in range(x):
        ogrenciEkle()

#Listedeki tüm öğrencileri tek tek ekrana yazdıran
def ogrenciYazdir():
    for ogrenci in ogrenciler:
        print(ogrenci)

# Öğrencinin listedeki index numarası öğrenci numarası olarak 
#  kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
def ogrenciNo():
    studentNumber= input("Numarasını öğrenmek istediğiniz öğrencinin adını giriniz!: ")
    print(ogrenciler.index(studentNumber))

#Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
def cokluOgrenciSilme ():
    adet = input ("Kaç adet öğrenci silinecektir: ")
    i = 0
    while i<int(adet) :
        ogrenci = input ("İsim ve soyisim giriniz: ")
        ogrenciler.remove(ogrenci)
        if i == adet:
            break
        i +=1

ogrenciNo()
cokluOgrenciSilme()
ogrenciEkle()
ogrencilerEkle()
ogrenciSilme()
