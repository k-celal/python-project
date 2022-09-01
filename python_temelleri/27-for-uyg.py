# sayilar = [1,3,5,7,12,19,21]
# for i in sayilar:
#     if(i%3==0):
#         print(i)
# top=0
# for i in sayilar:
#     top=top+i

# print(top)

# for i in sayilar:
#     if(i%2==1):
#         print(i*i)

# sehirler=["kocaeli","istanbul","ankara","izmir","rize"]
# for i in sehirler
#     if len(i)<=5:
#         print(i)
        
# for i in sehirler:
#     harfsayi=0
#     for a in  i:
#         harfsayi+=1
#     if(harfsayi<=5):
#         print(i)    




urunler=[
    {"name":"samsung s6", "price":"3000"},
    {"name":"samsung s7", "price":"4000"},
    {"name":"samsung s8", "price":"5000"},
    {"name":"samsung s9", "price":"6000"},
    {"name":"samsung s10", "price":"7000"}
]
toplam=0
for urun in urunler:
    fiyat=int(urun["price"])
    toplam+=fiyat
print(toplam)
for urun in urunler:
    fiyat=int(urun["price"])
    if fiyat<=5000:
        print(urun["name"])
        

        
            