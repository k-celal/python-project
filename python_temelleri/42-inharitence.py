class Person:
    def __init__(self,name,lastname,age):
        self.name = name
        self.lastName = lastname
        self.age = age

    def eat(self):
        print('I am eating')

    def drink(self):
        print('I am drinking')

    def run(self):
        print('I am running')
class Student(Person):
  def __init__(self, name, lastname, age,number):
        Person.__init__(self,name, lastname, age)
        self.number= number
class Teacher(Person):
  def __init__(self, name, lastname, age,brancha):
        super().__init__(name, lastname, age)
        self.brancha=brancha
        


p1 = Person("Çınar","Turan",3)
s1 = Student("Yiğit","Bilgi",12,"584")
t1 = Teacher("Sadık","turan",36,"Biology")

print(p1.name+' '+p1.lastName+' '+str(p1.age))  # Çınar Turan 3
print(s1.name+' '+s1.lastName+' '+str(s1.age) +" "+s1.number)  # Yiğit Bilgi 12
print(t1.name+' '+t1.lastName+' '+str(t1.age) + " " + t1.brancha)  # Sadık turan 36