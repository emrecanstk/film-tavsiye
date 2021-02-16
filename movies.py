bilgilendirme = """
Geliştirici: Emre Can Satık
Adres: https://www.github.com/emrecanstk
Program Sürümü 1.2 """
print(bilgilendirme+"\n")
from math import *
from os import close
user_list,film_list,begeni_list,aksiyon_list,komedi_list,korku_list = [],[],[],[],[],[]
tavsiye_list,tfilm_list,tbegeni_list,taksiyon_list,tkomedi_list,tkorku_list = [],[],[],[],[],[]
dict1,dict2,farklar = {},{},list()

filmler = open("C:\\Repo\\film-tavsiye\\veri_filmler.txt","r",encoding="utf-8")
fs = filmler.read().count("\n")  # fs = film sayısı
filmler.close()

def veriler():     # KENDİ DOSYA YOLUNUZU YAZINIZ.       # film listemizi parçalar halinde alıyoruz
    with open("C:\\Repo\\film-tavsiye\\veri_filmler.txt","r",encoding="utf-8") as filmler:
        for satir in filmler:
            satir = satir[:-1]
            liste = satir.split(":")        # her bir satır için filmlerle puanları birbirinden ayırdık.
            film_isim = liste[0]            # filmin ismini yakaladık.
            film_list.append(film_isim)     # film isimlerini listeye ekliyoruz.
            puanlar = liste[1].split(",")   # puanları aradaki virgüllere göre ayırdık.
            aksiyon = int(puanlar[0])
            aksiyon_list.append(aksiyon)
            komedi = int(puanlar[1])
            komedi_list.append(komedi)
            korku = int(puanlar[2])
            korku_list.append(korku)

def tveriler():     # KENDİ DOSYA YOLUNUZU YAZINIZ.      # yukarıdaki işlemleri tavsiye filmler için de uyguluyoruz 
    with open("C:\\Repo\\film-tavsiye\\veri_tavsiye.txt","r",encoding="utf-8") as tavsiyeler:
        for satir in tavsiyeler:
            satir = satir[:-1]
            liste = satir.split(":")
            film_isim = liste[0]
            tfilm_list.append(film_isim)
            puanlar = liste[1].split(",")
            aksiyon = int(puanlar[0])
            taksiyon_list.append(aksiyon)
            komedi = int(puanlar[1])
            tkomedi_list.append(komedi)
            korku = int(puanlar[2])
            tkorku_list.append(korku)

veriler()  # verileri çağırdık
tveriler() # verileri çağırdık

def tercih_belirt():
    for i in film_list:
        begeni = int(input(f"{i} filmini ne kadar beğeniyorsun: "))
        begeni_list.append(begeni)

def tercih_kaydet(): # ileriki aşamada programın kendisini düzenleyebilmesi için verilerin tutulması:
    user_isim = input("isminiz: ")
    user_list.append(user_isim)
    with open("C:\\Repo\\film-tavsiye\\veri_tercihler.txt","a",encoding="utf-8") as tercihler:
        a = 0          # KENDİ DOSYA YOLUNUZU YAZINIZ.
        while a<fs:
            tercihler.write(f"{user_isim}:{film_list[a]}:{begeni_list[a]}\n")
            a += 1

def tavsiye_yap():
    a,b,d = 0,0,0
    aksiyon_score,komedi_score,korku_score,tavsiye_score,tfilmler_dict = [],[],[],[],{}
    toplam_aksiyon,toplam_komedi,toplam_korku,toplam_aksiyon_score,toplam_komedi_score,toplam_korku_score = 0,0,0,0,0,0

    while a<fs:
        toplam_aksiyon += aksiyon_list[a]
        toplam_komedi += komedi_list[a]
        toplam_korku += korku_list[a]
        aksiyon_score.append(aksiyon_list[a] * begeni_list[a])
        komedi_score.append(komedi_list[a] * begeni_list[a])
        korku_score.append(korku_list[a] * begeni_list[a])
        toplam_aksiyon_score += aksiyon_score[a]
        toplam_komedi_score += komedi_score[a]
        toplam_korku_score += korku_score[a]
        a += 1
    
    aksiyon_istek = toplam_aksiyon_score / toplam_aksiyon
    komedi_istek = toplam_komedi_score / toplam_komedi
    korku_istek = toplam_korku_score / toplam_komedi

    while b<fs:
        tavsiye_score.append((aksiyon_istek*taksiyon_list[b])+(komedi_istek*tkomedi_list[b])+(korku_istek*tkorku_list[b]))
        tfilmler_dict[tavsiye_score[b]] = tfilm_list[b]
        b += 1

    tavsiye_score.sort()
    tavsiye_score.reverse()

    while d<fs:
        tavsiye_list.append(tfilmler_dict[tavsiye_score[d]])
        print(f"{d+1}- {tavsiye_list[d]}")
        d += 1

def tavsiye_degerlendir():
    for i in tavsiye_list:
        begeni = int(input(f"{i} filmi tavsiyesini ne kadar begendin: "))
        tbegeni_list.append(begeni)

def raporlar():
    tespit_basari = 0.0
    a,b,c,d=0,0,0,0

    while a<fs:
        dict1[tbegeni_list[a]] = a+1
        a += 1
    
    tbegeni_list.sort()
    tbegeni_list.reverse()

    while b<fs:
        dict2[tbegeni_list[b]] = b+1
        b += 1

    while c<fs:
        fark = dict1[tbegeni_list[c]] - dict2[tbegeni_list[c]]
        farklar.append(abs(fark))
        c += 1

    toplam_fark = 0
    while d<12:
        toplam_fark += farklar[d]
        d += 1

    a,toplam = 2,0
    while a<=fs:
        bir_eksik = a-1
        while bir_eksik > 0:
            toplam += bir_eksik
            bir_eksik -= 2
        max_fark = toplam*2
        toplam = 0
        a += 1

    tespit_basari = 100 - ((100*toplam_fark)/max_fark)

    tespit_basari = round(tespit_basari,2)
    with open("C:\\Repo\\film-tavsiye\\veri_raporlar.txt","a") as raporlar:  # raporların kaydedilmesi
        raporlar.write(str(tespit_basari)+" ")  
    
    print("Bu çalıştırma için başarı oranı: %"+str(tespit_basari)+"\n")
    
print("\n--Aşağıdaki filmleri tam sayılar kullanarak puanlayınız--\n")
tercih_belirt()
print("\n--Belirttiğiniz tercihleri isminizle kaydediniz--\n--Not:Bu işlem programın ileriki sürümlerinde programın kendini düzenleyebilmesine katkı sağlayacaktır--\n")
tercih_kaydet()
print("\n--Beğenilerinize göre 12 filmlik bir listenin sizin için sıralanmış hali--\n")
tavsiye_yap()
print("\n--Yapılan film tavsiyelerini tam sayılarla değerlendir--\n")
tavsiye_degerlendir()
print("\n--Raporlar--\n")
raporlar()