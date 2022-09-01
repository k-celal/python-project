from unicodedata import name


names=["ali","yağmur","hakan","deniz"]
years=[1998,2000,1998,1987]
names.append("cenk")
names.insert(0,"sena")
print(names.index("deniz"))
names.remove("deniz")
print("ali" in names)
names.reverse()
names.sort()
years.sort()
str="chevrolet,dacia"
result= str.split(",")
print(result)

min=min(years)
max=max(years)
print(min,max)
print(years.count(1998))
years.clear()
print(names)
print(years)
markalar=[]
markalar.append(input("1.markayı giriniz"))
markalar.append(input("2.markayı giriniz"))
markalar.append(input("3.markayı giriniz"))
print(markalar)
