#method
list=[1,2,3]
list.append(4)#bunlar method
#function
def sayhello(name="user"):
    return ("Hello"+name)
print(sayhello("Celal"))
def total(num1,num2):
    '''
    DOCSTRİNG: Toplama yapan fonksiyon
    INPUT:Iki adet sayi
    OUTPUT:Sayilarin toplami
    '''
    return num1+num2
help(total)