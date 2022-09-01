car_list=["bmw","mercedes","opel","mazda"]
print(len(car_list))
print(car_list[0],car_list[len(car_list)-1])
car_list[3]="toyota"
print(car_list)
result="mercedes" in car_list
result=car_list[-2]
result=car_list[0:3]
car_list[-2:]=["toyota","renault"]
# car_list.append("nissan")
# car_list.append("audi")
result=car_list+["audi","nissan"]
del car_list[len(car_list)-1]
result=car_list[::-1]
print(car_list)
print(result)
print("------------------------------------")
studentA=["Yiğit ","bilgi" ,"2010",[70,60,70]]
studentB=["sena ","turan" ,"1999",[80,80,70]]
studentC=["ahmet","turan" ,"1998",[80,70,90]]
students=[studentA,studentB,studentC]
print(students[0][0][0])
istek=input("Kaçıncı öğrenciyi istiyorsunuz")
print(students[int(istek)][0])
ortalama=(students[int(istek)][3][0]+students[int(istek)][3][1]+students[int(istek)][3][2])/3
result=f"{students[int(istek)][0]} {students[int(istek)][1]} {2019-int(students[int(istek)][2])} yaşında ve not ortalaması {ortalama}"
print(result)


