name = "celal"
surname='karahan '# "" veya '' olur farketmez
age = 36

greeting="My name is " + name + " " + surname +  " and \n I am " + str(age)+  "years old"

print(greeting)
print(greeting[0])
print(len(greeting))
print(greeting[len(greeting)-1])
print(greeting[-1])#üsttekiyle aynı işlevi görür
print(greeting[2:7])
print(greeting[:7])
print(greeting[3:])
print(greeting[2:40:2])

