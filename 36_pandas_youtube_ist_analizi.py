import pandas as pd

df = pd.read_csv("veri_setleri/DEvideos.csv")

islem = df
islem = df.head(10)
islem = df[5:10].head()
islem = len(df.columns)
df.drop(["video_error_or_removed", "description", "ratings_disabled", "comments_disabled", "thumbnail_link"], axis= 1, inplace= True)
islem = df
islem = df["likes"].mean()
islem = df["dislikes"].mean()
islem = df.head(50)[["title", "likes", "dislikes"]]
islem = df["views"].max()
islem = df["views"].min()
islem = df[df["views"].max() == df["views"]][["title", "views"]]
islem = df[df["views"].max() == df["views"]]["title"].iloc[0]
islem = df[df["views"].min() == df["views"]]["title"].iloc[0]
islem = df.sort_values("views", ascending= False).head(10)[["title", "views"]]
islem =df.groupby("category_id").mean().sort_values("likes")["likes"]
islem =df.groupby("category_id").mean().sort_values("likes", ascending= False)["likes"]
islem = df.groupby("category_id").sum().sort_values("comment_count", ascending= False)["comment_count"]
islem = df["category_id"].value_counts()
df["title_len"] = df["title"].apply(len)
islem = df
df["tag_count"] = df["tags"].apply(lambda x: len(x.split("|")))

def likeDislikeOranHesapla(veriseti):
    likesList = list(veriseti["likes"])
    dislikesList = list(veriseti["dislikes"])

    liste = list(zip(likesList, dislikesList))
    oranListesi = []
    for like, dislike in liste:
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like / (like + dislike))
    return oranListesi

df["begeni_orani"] = likeDislikeOranHesapla(df)
print(df.sort_values("begeni_orani", ascending= False)[["title", "likes", "dislikes", "begeni_orani"]])

# print(islem)