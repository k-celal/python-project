numbers=[10,15,12,13]
for a in numbers:
    print(a) 
    
tuple=[(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple:
    print(a,b)    

d={"k1":1,"k2":2,"k3":3}
for item in d:
    print(item)

for item in d.items():
    print(d)
    
for key,value in d.items():
    print(key,value)