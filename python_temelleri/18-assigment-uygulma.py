import re


x,y,z=2,5,10
numbers=1,5,7,10,6

num1=int(input("1.sayıyı giriniz"))
num2=int(input("2.sayıyı giriniz"))

reply=(num1*num2)-(x+y+z)
print(reply)
reply=y//x
print(reply)
reply=(x+y+z)%3
print(reply)
reply=y**x
print(reply)
x,*y,z=numbers
reply=z**3
print(reply)
reply=0
for i in  y:
    reply+=i
    
print(reply)
    