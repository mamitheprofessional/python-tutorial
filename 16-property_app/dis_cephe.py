import math

deniz_kenari = 2
sehir_merkezi = 1.5
tasra = 0.75

def puanlama(puan, konum, dis_cephe_stil):
    euler_sayisi = math.e
    pi_sayisi = math.pi
    

    def modern_cephe(puan):
        if dis_cephe_stil == 1:
            return puan * puan

    def geleneksel_cephe(puan):
        if dis_cephe_stil == 2:
            return puan * pi_sayisi

    def eski_cephe(puan):
        if dis_cephe_stil == 3:
            return puan * euler_sayisi

    if dis_cephe_stil == 1:
        if konum == 1:
            return modern_cephe(puan) * deniz_kenari * 500
        elif konum == 2:
            return modern_cephe(puan) * sehir_merkezi * 500
        elif konum == 3:
            return modern_cephe(puan) * tasra * 500
    elif dis_cephe_stil == 2:
        if konum == 1:
            return geleneksel_cephe(puan) * deniz_kenari * 500
        elif konum == 2:
            return geleneksel_cephe(puan) * sehir_merkezi * 500
        elif konum == 3:
            return geleneksel_cephe(puan) * tasra * 500
    elif dis_cephe_stil == 3:
        if konum == 1:
            return eski_cephe(puan) * deniz_kenari * 500
        elif konum == 2:
            return eski_cephe(puan) * sehir_merkezi * 500
        elif konum == 3:
            return eski_cephe(puan) * tasra * 500