import time
import datetime as d


try:
    il = int(input('Dogum ili: '))
    ay = int(input('Dogum ayi: '))
    gun = int(input('Dogum gunu: '))
    ad_gunu = d.date(il, ay, gun)
except ValueError:
    print('Doğum günü tarixi yanlishdir')
else:
    tarix = d.datetime.now()
    bu_il = tarix.year
    ad_gunu_bu_il = d.date(bu_il , ay , gun)


    if ad_gunu_bu_il < tarix.date():
        novbeti_ad_gunu = d.date(bu_il + 1, ay, gun)
    else:
        novbeti_ad_gunu = ad_gunu_bu_il

    qalan_gun = (novbeti_ad_gunu - tarix.date()).days

    if qalan_gun == 0:
        print('Ad gününüzdür')
    else:
        print('Ad gününüzə ' +str(qalan_gun)+ ' gün qalib.')
