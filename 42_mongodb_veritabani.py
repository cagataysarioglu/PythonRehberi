import pymongo
from bson.objectid import ObjectId # Kimlik numarası ile süzgeçleme yapabilmek için.

istemci = pymongo.MongoClient("mongodb://localhost:27017")

veritabanim = istemci["ultur-vt"]
koleksiyonum = veritabanim["urunler"]

# print(istemci.list_database_names())
# print(veritabanim.list_collection_names())

####### EKLEME ###############################################################################

# urun = {"ad": "MSI GP62", "fiyat": 7000}
# islem = koleksiyonum.insert_one(urun)

# print(islem)
# print(type(islem))
# print(islem.inserted_id)

# urunListesi = [
#     {"ad": "MSI GP64", "fiyat": 7300}, # "_id": 1 vb. yazım ile kimliği biz verebiliriz.
#     {"ad": "MSI GP50", "fiyat": 5000},
#     {"ad": "MSI GT60", "fiyat": 8000},
#     {"ad": "MSI GTX70", "fiyat": 9400},
#     {"ad": "MSI GS35", "fiyat": 4500}
# ]

# urunListesi = [
#     {"ad": "MSI GT79", "fiyat": 7900, "hdd": "1 TB"},
#     {"ad": "MSI GP69", "fiyat": 6400, "hdd": "1 GB"},
#     {"ad": "MSI GP70", "fiyat": 6800, "kategori": ["Bilgisayar", "Elektronik"]}
# ]

# islem = koleksiyonum.insert_many(urunListesi)
# print(islem.inserted_ids)

####### SEÇME ################################################################################

# islem = koleksiyonum.find_one() # İlk kaydı döndürür.

# for i in koleksiyonum.find(): # "*"daki gibi hepsini döndürür.
#     print(i)

# for i in koleksiyonum.find({}, {"_id":0, "kategori":0}): # Boş {} ile tamamını istedik, 0 ve 1 ise olsun ya da olmsın dedik.
#     print(i)

####### FİLTRELEME #############################################################################

suzgec = {"fiyat": 7000} # Süzgecimiz (Filtremiz)

# islem = koleksiyonum.find({"hdd": "1 TB"})
# for i in islem:
#     print(i)

# islem = koleksiyonum.find(suzgec)
# for i in islem:
#     print(i)

# islem = koleksiyonum.find_one(suzgec) # Kıstasa uyan ilk yadı döndürür.
# print(islem)

# islem = koleksiyonum.find_one({"_id": ObjectId("5f8c7cf70f575b2cb8b96415")})
# print(islem)

# islem = koleksiyonum.find({
#     "ad": {
#         "$in": ["MSI GP62", "MSI GP69"]
#     }
# })
# for i in islem:
#     print(i)

# islem = koleksiyonum.find({
#     "fiyat": {
#         "$gt": 6000
#     }
# })

# # $gt: Greater than (Büyük)
# # $gte: Greater than equal (Büyük eşit)
# # $eq: Equal (Eşit)
# # $ne: Not equal (Eşit değil)
# # $lt: Less than (Küçük)
# # $lte: Less than equal (Küçük eşit)
# # $regex: Regular expression (Düzenli ifade)

# islem = koleksiyonum.find({
#     "ad": {"$regex": "^M"}
# })
# for i in islem:
#     print(i)

####### SIRALAMA #########################################################################

# islem = koleksiyonum.find().sort("fiyat") # Varsayılan hâli artandır.
# for i in islem:
#     print(i)

# islem = koleksiyonum.find().sort("ad") # ("ad", 1) ile artan, ("ad", -1) ile azalan şeklinde de kullanılabilir.
# for i in islem:
#     print(i)

# islem = koleksiyonum.find().sort([("ad", 1), ("fiyat", -1)])
# for i in islem:
#     print(i)

####### GÜNCELLEME #########################################################################

# koleksiyonum.update_one(
#     {"ad": "MSI GTX70"},
#     {"$set": {
#         "ssd": "500 GB"
#     }}
# )

# koleksiyonum.update_many(
#     {}, # Hepsini seçtim.
#     {"$set": {
#         "kategori": ["Bilgisayar", "Elektronik"]
#     }}
# )

# koleksiyonum.update_many(
#     {"ad": "MSI GP62"},
#     {"$set": {
#         "hdd": "1 TB"
#     }}
# )

# sorgu = {"ad": "MSI GP50"}
# yeniDeger = {"$set": {
#                 "hdd": "500 GB",
#                 "fiyat": 5200
#             }}
# sonuc = koleksiyonum.update_many(sorgu, yeniDeger) # Bu biçimde de yapılabilir.
# print(f"{sonuc.modified_count} adet kayıt güncellendi.")

# for i in koleksiyonum.find():
#     print(i)

####### SİLME ##################################################################################

# koleksiyonum.delete_one({"ad": "MSI GI90"}) # İlk ilgili kaydı siler.
# koleksiyonum.delete_many({"ad": "MSI FX90"}) # İlgili tüm kayıtları siler.
# koleksiyonum.delete_many({"ad": {"$regex": "^A"}}) # Adı A harfiyle başlayan tüm kayıtları siler.

# sonuc = koleksiyonum.delete_many({}) # Bütün kayıtları siler.
# print(f"{sonuc.deleted_count} adet kayıt silindi.")