def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(":")
    ogrenci_Adi=liste[0]
    notlar=liste[1]
    notlar=notlar.split(",")
    top_not=0
    for nots in notlar:
        top_not+=int(nots)
    
    ort_not=top_not/len(nots)
    if ort_not>=90 and ort_not<=100:
        harf = "AA"
    elif ort_not>=85 and ort_not<=89:
        harf = "BA"
    elif ort_not>=80 and ort_not<=84:
        harf = "BB"
    elif ort_not>=75 and ort_not<=79:
        harf = "CB"
    elif ort_not>=70 and ort_not<=74:
        harf = "CC"
    elif ort_not>=65 and ort_not<=69:
        harf = "DC"
    elif ort_not>=60 and ort_not<=64:
        harf = "DD"
    elif ort_not>=50 and ort_not<=59:
        harf = "FD"
    else:
        harf = "FF"
    return ogrenci_Adi + ": " + harf + "\n"      
    
def notları_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
        
def not_gir():
    ad=input("Ogrenci Adı: ")
    soyad=input("Ogrenci Soyadı: ")
    not1=input("Ogrenci Notu ")
    not2=input("Ogrenci Notu ")
    not3=input("Ogrenci Notu ")
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad + " "+ soyad + ":" + not1+","+not2+","+not3+"\n")
def notları_kayıt_Et():
    with open("sinav_notlari.txt","r",encoding="utf-8")as file:
        liste=[]
        for i in file:
            liste.append(not_hesapla(i))
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)
while True:
    islem=input("1-Notları Oku\n2-Not Gir\n3-Notları Kayıt Et\n4-Çıkıs\nSecim: ")
    if islem=="1":
        notları_oku()
    elif islem=="2":
        not_gir()
    elif islem=="3":
        notları_kayıt_Et()
    elif islem=="4":
        break
    else:
        print("Yanlıs secim lutfen 1,2,3,4 arasından secim yapınız")       