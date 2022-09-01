# sehirler=["niğde","ankara"]
# plakalar=[51,6]
# print(plakalar[sehirler.index("niğde")])

# plakalar={"kocaeli":41,"niğde":51}
# print(plakalar["kocaeli"])
# plakalar["istanbul"]=34
# print(plakalar["istanbul"])
# plakalar["kocaeli"]="new value"
from calendar import c


users={
    "celalkarahan":{
        "age":36,
        "roles":["user"],
        "email":"celal51kara@gmail.com",
        "adres":"niğde",
        "phone":"05362440815"
        },
    "bahadırkarahan":{
        "age":8,
        "roles":["admin","user"],
        "email":"baho51kara@gmail.com",
        "adres":"niğde",
        "phone":"05362256315"
        },
}
print(users["celalkarahan"]["age"])
print(users["celalkarahan"]["roles"][0])
