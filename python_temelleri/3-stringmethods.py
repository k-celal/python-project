from email import message_from_string


message = "hello there . my name is celal karahan"

message=message.upper()
print(message)
message=message.title()
print(message)
message=message.lower()
print(message)
message=message.capitalize()
print(message)
message=message.strip()
print(message)
message=message.split()
print(message)
message="**".join(message)
print(message)
index= message.find("celal")
print(index)
index= message.find("celall")
print(index)
isfound=message.startswith("H")
print(isfound)
isfound=message.startswith("B")
print(isfound)
message = "hello there . my name is celal karahan"
message=message.replace("celal","Hasan")
print(message)
message=message.center(100,"*")
print(message)