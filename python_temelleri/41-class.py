# class Person:
#      # class attributes
#     address = 'no information'
#     name="no information"
#      # constructor (yapıcı metod)
#     def __init__(self, name, year):

#          # object attributes
#          self.name = name
#          self.year = year
#     #method
#     def greeting(self):
#         print(f"hello : {self.name}")
#     def calculateAge(self):
#         return 2020 - self.year  
         
# p1 = Person(name='ali', year= 1990) 
# p2 = Person(name ='yağmur', year = 1995)

# p1.name = 'ahmet'
# p1.address = 'kocaeli' 

# print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}') # adım: ali ve yaşım: 30
# print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}') # adım: yağmur ve yaşım: 25
# p1.greeting()

from calendar import c


class Circle():
    pi=3,14
    def __init__(self,yaricap=1):#eğer yaricap degeri gönderilmez ise  1 olarak tanımlanır
        self.yaricap=yaricap
    
    def alanhesap(self):
        return self.pi*(self.yaricap**2)
    def cevrehesap(self):
        return self.pi*(self.yaricap)*2

c1=Circle(5)
print(f"alan : {c1.alanhesap()} cevre : {c1.cevrehesap()}")