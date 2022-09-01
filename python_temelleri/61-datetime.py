from datetime import datetime
# from datetime import time 
# from datetime import date
from datetime import timedelta


now= datetime.now()#now yerine today da kullanılır
result = now.day
result=now.month
result=datetime.ctime(now)
result=datetime.strftime(now,"%Y")
result=datetime.strftime(now,"%X")
result=datetime.strftime(now,"%A")
result=datetime.strftime(now,"%B")
result=datetime.strftime(now,"%d")

# t="21 Nisan 2019"
# gun,ay,yıl=t.split()
t="15 April 2019 hour 10:12:30"
dt=datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
print(dt)

birthday=datetime(2003,10,28)
result=datetime.timestamp(birthday)
result=datetime.fromtimestamp(result)
result = datetime.fromtimestamp(0)

result = now - birthday # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(now)

# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730, minutes = 10)

result = now - timedelta(days = 10)

print(result)
print(result)