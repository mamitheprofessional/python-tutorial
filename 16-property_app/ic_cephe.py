luks = 5
guzel = 3
idare_eder = 1.5

def ic_mekan_fiyat_hesabi(en, boy, ic_mekan_tasarimi):
    def metre_kare(en, boy):
        return en * boy

    if ic_mekan_tasarimi == 1:
        ic_fiyat = metre_kare(en, boy) * luks * 1000
    elif ic_mekan_tasarimi == 2:
        ic_fiyat = metre_kare(en, boy) * guzel * 1000
    elif ic_mekan_tasarimi == 3:
        ic_fiyat = metre_kare(en, boy) * idare_eder * 1000
    else:
        print("Yanlış tuşlama yaptınız")
        return None

    return ic_fiyat