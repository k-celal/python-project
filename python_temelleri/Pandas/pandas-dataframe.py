#serilerin birleşmiş halidir
import pandas as pd

# s1=pd.Series([3,2,1,0])
# s2=pd.Series([0,3,7,2])
# data=dict(apples=s1,oranges=s2)
# df= pd.DataFrame(data)
# df= pd.DataFrame([1,2,4,5])
data=[["Ahmet",50],["enes",30],["mehmet",80],["cınar",70]]
dict={"Name":["Ahmet","Enes","Mehmet","Cınar"],"Grade":[50,60,70,80]}
dict_list=[
    {"Name":"Ahmet","Grade":"50"},
    {"Name":"Enes","Grade":"30"},
    {"Name":"Mehmet","Grade":"80"},
    {"Name":"Ahmet","Grade":"70"}  
]
df= pd.DataFrame(data,columns=["name","grade"],index=[1,2,3,4],dtype=float)
df=pd.DataFrame(dict,index=["212","213","214","214"]) 
df=pd.DataFrame(dict_list)
df=pd.DataFrame(dict_list,index=["212","213","214","214"])

print(df)

