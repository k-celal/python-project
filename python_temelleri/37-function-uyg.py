# def yazdir(kelime="none",kackez=1):
#     a=0
#     while(a<kackez):
#         print(kelime)
#         a+=1    
# yazdir("Celal",5)



# def listele(*args):
#     n=[]
#     for i in args:
#         n.append(i)
#     return n
# print(listele(3,5,6,8,9,2,1,6,8))

# def asalmı(sayi):
#     a=2
#     if(sayi==1):return-1
#     if(sayi==2):return 2
#     while a<sayi:
#         if(sayi%a==0):
#             return -1
#         a+=1
#     return sayi
    
    
# def asalbul(bas,son):
#     n=[]
#     while bas<son:
#         if(asalmı(bas)==bas):n.append(bas)
#         bas+=1
#     return n    
# print(asalbul(5,15))

def bolenbul(sayi):
    a=1
    bolenler=[]
    while a<sayi:
        if sayi%a==0:
            bolenler.append(a)
        a+=1
    bolenler.append(sayi)
    return bolenler

print(bolenbul(18))