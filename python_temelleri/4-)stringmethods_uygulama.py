import re


website="http://www.sadikturan.com"
course="Python Kursu: Baştan sona python programlama rehberi (40 saat)"
print(' hello world '.strip())
result=website.strip("w.mochtp:/")
print(result)
result=course.lower
print(result)
result=website.count("a")
print(result)
result=website.startswith("www")
result2=website.endswith("com")
print(result,result2)
result=website.find('com')
result2=website.find('com',0,10)#bulamazssa -1 .ıkar
print(result,result2)
result=website.index('com')#bulamazssa hata çıkar
print(result)
result=course.isalpha()
result2=course.isdigit
print(result,result2)
result="contents".center(50,"*")
result2="contents".ljust(50,"*")
print(result,result2)
result=course.replace(" ","-")
result2=course.replace(" ","-",5)
print(result,result2)
result="hello world".replace("world","there")
print(result)
result=course.split(" ")
print(result)

