# liste = [1,2,3,4,5]
# iterator=iter(liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# liste = [1,2,3,4,5]
# iterator=iter(liste)
# while True:
#     try:
#         item=next(iterator)
#         print(item)
#     except StopIteration:
#         break
class Mynumber:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=self.stop:
            x=self.start
            self.start+=1
            return x
        else:
            raise StopIteration
list=Mynumber(10,20)

for x in list:
    print(x)
