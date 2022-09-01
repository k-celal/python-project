fruits={"orange","apple","banana"}
# print(fruits[0])indeklenemez
for x in fruits:
    print(x)

fruits.add("cherry")
fruits.update(["mango","grape","apple"])    
#eleman sadece  kere olabilir
fruits.remove("mango")
fruits.discard("apple")
fruits.pop#rastgele silr
fruits.clear#hepsini siler
number={1,2,3,69,1,2}
print(set(number))