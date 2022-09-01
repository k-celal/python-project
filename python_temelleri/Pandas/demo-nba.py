import pandas as pd
# 1- İlk 10 kaydı getiriniz.
# 2- Toplam kaç kayıt vardır ?
# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?
# 4- En yüksek maaşı ne kadardır ?
# 5- En yüksek maaşı alan oyuncu kimdir ?
# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
# 9- Kaç farklı takım mevcut ?
# 10- Her takımda kaç oyuncu oynamaktadır ?
# 11- İsmi içinde "and" geçen kayıtları bulunuz.
df=pd.read_csv('C:/Users/Celal/Documents/pythonProject/python_temelleri/Pandas/datasets/nba.csv')
# result=df.head(10)
# result=df.columns
result = len(df.index)# result=df.info()
result=df["Salary"].mean()
result=df["Salary"].max()
result = df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]
result=df[(df["Age"]<=25.0) & (df["Age"]>=20.0)][["Name","Team","Age"]].sort_values("Age",ascending=False)
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]
result=df.groupby("Team").mean()["Salary"]
result=len(df.groupby("Team"))
result=df["Team"].nunique()
result = df["Team"].value_counts()
df.dropna(inplace = True)#Nan Alanları silme inplace true ise aynı dataframe içinde siler
# result = df[df["Name"].str.contains("and")]
def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["Name"].apply(str_find)]

print(result)