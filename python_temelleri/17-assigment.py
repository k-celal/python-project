x=5
z=5
y=5
x,y,z=5,1,3
x+=10
x-=10
x*=10
x/=10
x%=9
x//=5#sadece tam kısmı verir
x**=5#üs alma işlemi

values=1,2,3
print(type(values))
x,y,z=values
print(x,y,z)

print("------------------")
value=1,2,3,5,64,4
# x,y,z=value#fazla değere eşitlendiği çin hata
x,y,*z=value#hata vermez çünkü z dizi biçiminde tanımlanmış
print(x,y,z)
