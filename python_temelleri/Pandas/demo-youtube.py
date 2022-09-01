import pandas as pd
# 1- İlk 10 kaydı getiriniz.
# 2- İkinci 5 kaydı getiriniz.
# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
# 7- En çok görüntülenen video hangisidir ?
# 8- En düşük görüntülenen video hangisidir?
# 9- En fazla görüntülenen ilk 10 video hangisidir ?
# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
# 12- Her kategoride kaç video vardır ?
# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)
df=pd.read_csv('C:/Users/Celal/Documents/pythonProject/python_temelleri/Pandas/datasets/youtube-ing.csv')
result=df.head()
result=df[5:].head()
result=df.columns
result=len(df.columns)
result=df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1)
result=df["likes"].mean()
result=df["dislikes"].mean()
result=df[0:50][["likes","dislikes"]]
result=df[df["views"]==df["views"].max()]["title"].iloc[0]
result=df[df["views"]==df["views"].min()]["title"].iloc[0]
result=df.sort_values("views",ascending=False).head(10)[["title","views"]]
result=df.groupby("category_id").mean().sort_values("likes",ascending=False)["likes"]
result=df.groupby("category_id").mean().sort_values("comment_count",ascending=False)["comment_count"]
result=df["category_id"].value_counts()
df["title_len"] = df["title"].apply(len)
result=df["title_len"]
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))
def tagCount(tag):
    return len(tag.split('|'))
df["tag_count"] = df["tags"].apply(tagCount)
result=df["tag_count"]
# df["populer_video"]=df["likes"]/df["dislikes"]
# result=df.sort_values("populer_video",ascending=False)[["title","populer_video"]]
def likedislikeoranhesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))

    oranListesi = []

    for like,dislike  in liste: 
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"] = likedislikeoranhesapla(df)

print(df.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]])
print(result)
