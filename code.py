def sezar_sifreleme(metin, kaydirma_miktari):
    sifreli_metin=""
    for karakter in metin:
        if karakter.isalpha():
            ascii_offset=65 if karakter.isupper() else 97
            sifreli_metin +=chr((ord(karakter)-ascii_offset+kaydirma_miktari)%26+ascii_offset)
        
        else:
            sifreli_metin +=karakter 
            
    return sifreli_metin
def sezar_cozme(sifreli_metin,kaydirma_miktari):
    return sezar_sifreleme(sifreli_metin,-kaydirma_miktari)

metin=input("lutfen sifrelenecek metni giriniz:")
kaydirma_miktari=int(input("lutfen kaydirma miktarini giriniz(1-25):"))

sifreli_metin=sezar_sifreleme(metin,kaydirma_miktari)
print(f"sifrelenmis metin: {sifreli_metin}")

cozulmus=sezar_cozme(sifreli_metin,kaydirma_miktari)
print(f"cozulmus metin: {cozulmus}")
