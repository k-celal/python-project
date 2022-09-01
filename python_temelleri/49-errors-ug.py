# liste=["1","2","5a","10b","abc","10"]
# i=0
# while i<len(liste):
#     try:
#         liste[i]=int(liste[i])
#         i+=1
#     except:
#         i+=1
#         continue
    
# print(liste)    

# devam=""
# while devam!="q":
#     devam=input("Sayısal deger griniz cıkmak icin q")
#     if devam=="q":break
#     try:
#         devam=int(devam)
#         print(f"Girilen sayısal deger: {devam}")
#     except :
#         print("Sayısal deger girmelisiniz")
#         continue

# import re

# def check_psw(psw):
#     turkce_krk="üıİşçöğ"
#     for i in psw:
#         if i in turkce_krk:
#             raise TypeError("Parolada turkce karakter olmamalı")
#         else:
#             pass    
#     print("Gecerli parola")
    
# psw=input("Parola giriniz")
# try:
#     check_psw(psw)
# except TypeError:
#     print("Hatalı parola")

def faktoriyel(x):
    x= int(x)
    
    if x<0:
        raise ValueError("Negatif deger girmeyiniz")
    elif x==0:
        return 1
    a=1
    for i in range(1,x+1):
        a*=i
    return a

try:
    print(faktoriyel(0))
except ValueError as a:
    print(a)
    