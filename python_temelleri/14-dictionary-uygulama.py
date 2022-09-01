ogrenciler={
    "120":{
        "ad":"Celal",
        "soyad":"karahan",
        "telefon":"5356324152"
    },
    "141":{
        "ad":"Bahadır",
        "soyad":"karahan",
        "telefon":"5329327142"
    },
    "158":{
        "ad":"Hasan",
        "soyad":"karahan",
        "telefon":"5384229632"
    } 
}
no=input("Please students no: ")
name=input("Please students name: ")
surname=input("please student surname: ")
telephone=input("Please students telephone: ")
# ogrenciler[int(no)]={
#     "ad":name,
#     "soyad":surname,
#     "telefon":telephone
# }
ogrenciler.update({
    no:{
       "ad":name,
       "soyad":surname, 
       "telefon":telephone
    }
})
selection=input("Please enter the student number whose information you want to show: ")
name=ogrenciler[int(selection)]["ad"]
surname=ogrenciler[int(selection)]["soyad"]
telephone=ogrenciler[int(selection)]["telefon"]
print(f"Ogrencinin adı {name} \nOgrenci soyadı {surname} \nOgrenci telefon {telephone}")