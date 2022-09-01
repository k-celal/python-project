# global scope
from cgi import test


x = 'global x'

def function(): 
    # local scope
    # x = 'local x'
    print(x)

function() # local x
print(x)   # global x  
# global
name = 'Çınar'

def changeName(new_name):
    # local 
    name = new_name
    print(name)

changeName('Ada') # Ada
print(name)       # Çınar
name = 'global string'

def greeting():
    name = 'Çınar'

    def hello():
        print('hello '+ name)

    hello()

greeting() # hello Çınar
name = 'global string'

def greeting():
    name = 'Çınar'

    def hello():
        name = 'Ada'
        print('hello '+ name)

    hello()

greeting() # hello Ad

#################
x=50
def change():
    global x
    print(f'x : {x}')
    x=100
    print(f"changed x to {x}")

test()
print(x)