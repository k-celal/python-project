def changeName(n):
    n="ada"
changeName("Celal")
print("Celal")#celal değişmedi 

def change(n):
    n[0]="istanbul"
sehirler=["ankara","izmir"]
change(sehirler)
print(sehirler)#adres aynı olduğu içn içerik değişti    
#peki kopyalama işlemi nasıl yapılır
n=sehirler[:]
n[0]="istanbul"
print(sehirler)

# def add(*params):
#     return sum(params)
def displayUser(**args):
    for key,value in args.items():
        print("{} is {}".format(key,value))
        
displayUser(name="Celal",age=2,city="istanbul")
displayUser(name="Hasan",age=4,city="istanbul",mail="hasan@gmail.com")
displayUser(name="Esma",age=18,city="istanbul",phone="05362440815")
