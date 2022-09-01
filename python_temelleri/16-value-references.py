#value types
x=5
y=25
x=y
y=10
print(x,y)
#reference type
a=["apple","banana"]
b=["apple","banana"]
a=b
b[0]="grape"
print(a,b)
#adresler eşitlendiği için ikiside aynı adresi gösterir bundan dolayı biri değişince diğeri değişir