import random
random_num=int(random.random()*100)#random.randint(1,100) olabilridi
can_sayisi=5
puan=100
while True:
    if can_sayisi!=0:
        tahmin_sayi=int(input("Tahmin ettiğiniz sayi giriniz"))
        if(tahmin_sayi<random_num):
            print("sayiniz biraz küçük biraz büyütün")
            can_sayisi-=1
            puan-=20
        elif(tahmin_sayi>random_num):
            print("sayiniz biraz büyük biraz küçültün")
            can_sayisi-=1
            puan-=20
        else:
            print(f"Tebrikler {5-can_sayisi} denemede buldunuzz Puanınız : {puan}") 
    else:
        print("Canınız kalmadı")
        break
            