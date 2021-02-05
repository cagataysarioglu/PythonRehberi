IstemiHesap = {
    "ad": "İstemi Tuğrul",
    "hesapNu": "552347",
    "bakiye": 5000,
    "ekHesap": 2000
}
BuminHesap = {
    "ad": "Bumin Öztegin",
    "hesapNu": "639349",
    "bakiye": 3000,
    "ekHesap": 1000
}
def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if(hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı çekebilirsiniz.")
        bakiyeSorgulama(hesap)
    else:
        toplamPara = hesap['bakiye'] + hesap['ekHesap']
        if (toplamPara >= miktar):
            ekHesapKullanimi = input("Hesap bakiyeniz yetersiz, ek hesabınız kullanılsın mı? (E/H): ")
            if ekHesapKullanimi == "e":
                ekHesaptanKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] = ekHesaptanKullanilacakMiktar
                print(f"{hesap['hesapNu']} numaralı hesabınızın ek hesap bakiyesi {hesap['ekHesap']} Türk Lirasıdır.")
                bakiyeSorgulama(hesap)
            else:
                print("Ek hesabınızı kullanmamayı seçtiniz.")
        else:
            print("Bakiyeniz yetersizdir.")
            bakiyeSorgulama(hesap)
def bakiyeSorgulama(hesap):
    print(f"Bilgi: {hesap['hesapNu']} numaralı hesabınızda {hesap['bakiye']} Türk Lirası, ek hesabınızda ise {hesap['ekHesap']} Türk Lirası bulunmaktadır.")
paraCek(IstemiHesap, 4000)
print("***************************")
paraCek(IstemiHesap, 3000)
