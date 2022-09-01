class Movie():
    def __init__(self,name,director_name,duration):
        self.name=name
        self.director=director_name
        self.duration=duration
        print("film objesi oluşturuldu")
    def __str__(self):
        return f"{self.name} filmi bu {self.director} kişi tarafından yapıldı"
    def __len__(self):
        return self.duration
    def __del__(self):
        print(f"{self.name} silindi")
m=Movie("Harry Potter","Yönetmen",240)
print(m)
print(len(m))
del m