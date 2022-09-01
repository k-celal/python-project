# sayilar=[1,3,5,7,9,12,19,21]
# i=0
# while i<len(sayilar):
#     print(sayilar[i])
#     i+=1
# bas=int(input("lutfen bir baslangıc giriniz"))
# son=int(input("lutfen bir son giriniz"))
# while bas<son:
#     if bas%2==1:
#         print(bas)
#     bas+=1
# i=0
# sayilar=[]
# while(i<5):
#     sayilar.append(int(input(f"{i+1}. sayiyi giriniz")))
#     i+=1
# sayilar.sort()
# for i in sayilar:
#     print(i)
urun_sayi=int(input("Kaç urun gireceksiniz"))
i=0
urunler=[{}]
while i<urun_sayi:
    namee=input("Lutfen urun adı giriniz")
    pricee=input("Lutfen urunun fiyatını giriniz")
    urunler.append({"name":namee,"price":pricee})
    i+=1
a=0
while a<len(urunler):
    print(urunler[a])
    a+=1
    