import pandas as pd
from numpy.random import randn

df=pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])
result=df
result=df["Column1"]
result=df[["Column1","Column2"]]
# loc["row","column"] -> df.loc[:,["Column-1"]] en baştakiyle aynı
result=df.loc["A"]
result=df.loc[:,"Column1":"Column2"]#aralıkları verir
result=df.loc["B":"C","Column1":"Column2"]
result=df.iloc[2]
result=df.loc[["A","B"],["Column1"]]#kesişimleri gönderir
df["Column4"]=pd.Series(randn(3),["A","B","C"])
df["Column5"]=df["Column1"]+df["Column3"]
result=df
result=df.drop("Column5",axis=1,inplace=True)#inplace true yapılırsa df üzerinde de  değişiklik yapılır


print(result)