sayi=int(input("Asal olup olmadığını merak ettiğiniz sayiis giriniz: "))
bolen =2
if(sayi==2):
    print("Asaldır")
while bolen<sayi:
    if(bolen+1)==sayi:
        print("Asaldır")
    if(sayi%bolen==0):
        print("Asal degildir")
        break
    else:
        bolen+=1
