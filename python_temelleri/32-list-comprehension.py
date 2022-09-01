for x in range (10):
    print(x)
numbers=[a for a in range (10)]
print(numbers)
numbers=[x**2 for x in numbers]
print(numbers)
numbers=[x**2 for x in numbers if x%3==0]
print(numbers)

myString ="hello"
mylist=[letter for letter in myString]
print(mylist)
years=[1983,1999,2008,1956,1986]
ages = [2019-year for year in years]
print(ages)
result=[x if x%2==0 else "tek" for x in range(1,10)]
print(result)

numbers=[(x,y) for x in range(3) for y in range(3)]
print(numbers)