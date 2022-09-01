import os
import datetime

result = dir(os)
result = os.name

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

# klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/yeniklasör")

# listeleme
# result = os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


# etkin dizin öğrenme
# result = os.getcwd()


# result = os.stat("_datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

# os.system("cmd.exe")

# path

result = os.path.abspath("_os.py")
result = os.path.dirname("C:/Users/Celal/Documents/pythonProject/62-os.py")
result = os.path.dirname(os.path.abspath("62-os.py"))
result = os.path.exists("C:/Users/Celal/Documents/pythonProject/62-os1.py")#klasör varmı veya dosya vsrmı
result = os.path.exists("C:/Users/Celal/Documents/pythonProject")
result = os.path.isdir("C:/Users/Celal/Documents/pythonProject")
result = os.path.isfile("C:/Users/Celal/Documents/pythonProject/62-os.py")
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
# result = result[0]
result = result[1]

print(result)