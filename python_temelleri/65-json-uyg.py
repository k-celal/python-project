import json
import os
class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email
           
class  UserReporsitory:
    def __init__(self):
        self.users=[]
        self.isLoggedin=False
        self.curretUsser={}
        #load users from .json file
        self.loadusers()
        
    def loadusers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users= json.load(file)
                for usr in users:
                    usr = json.loads(usr)
                    newUser=User(username = usr["username"],password=usr["password"],email=usr["email"])
                    self.users.append(newUser)
                print(self.users)
    def register(self,user:User):
        self.users.append(user)
        self.savetofile()
        print("Kullanıcı olusturuldu")
    def login(self,username,password):
        for user in self.users:
            if user.username==username and user.password==password:
                self.isLoggedin=True
                self.curretUsser=user
                print("Giris yapıldı")
                break
    def logout(self):
        self.isLoggedin=False
        self.curretUsser={}
    def Idendtity(self):
        if self.isLoggedin:
            print(f"Kullanıcı Adı: {self.curretUsser.username} Mail: {self.curretUsser.email}")
        else:
            print("Giris Yapılmadı")        
    def savetofile(self):
        list=[]
        for user in self.users:
            list.append(json.dumps(user.__dict__))
            
        with open("Users.json","w") as file:
            json.dump(list,file)
            
def check_password(psw):
    import re
    if len(psw) <7:
        raise Exception("Parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]", psw):
        raise Exception("Parola küçük harf içermelidir.") 
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam içermelidir.")
    elif not re.search("[@!%&/=?_]", psw):
        raise Exception("Parola alpha numeric(@!%&/=?_) karakter içermelidir.")
    elif re.search("\s",psw):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Geçerli parola")

repository=UserReporsitory()    
while True:
    print("Menü".center(50,"*"))
    secim=input("1-Register\n2-Login\n3-Logout\n4-İdentity\n5-Exit\nSeçiminiz: ")
    if secim=="5":
        break
    elif secim=="1":
        username=input("Username: ")
        while True:
            try:
                password=input("Password: ")
                check_password(password)
            except Exception as re:
                print(re)
            else:break   
        email=input("Email: ")
        user=User(username=username,password=password,email=email)
        repository.register(user)   
    elif secim=="2":
        if repository.isLoggedin:
            print("Giris yapmak icin Once cikis yapiniz")
        else: 
            username=input("Username: ")
            password=input("Password: ")
            repository.login(username,password)
    elif secim=="3":
        repository.logout()
    elif secim=="4":
        repository.Idendtity()
        
        