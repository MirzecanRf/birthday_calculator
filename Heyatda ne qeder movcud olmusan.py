'''
Dogum ili: 1995
Dogum ayi: 11
Dogum gunu: 7

Sizin xxx yashiniz var
Siz heyatda xxx saniye, xxx deqiqe, xxx saat, xxx gundur ki movcudsunuz


'''
import time

import datetime as d 

from math import sqrt, ceil






try:
    il = int(input('Dogum ili: '))
    ay = int(input('Dogum ayi: '))
    gun = int(input('Dogum gunu: '))
except ValueError:
    print('Lutfen eded daxil edin')
else:
    tarix1 = d.datetime.now()
    tarix2 = d.datetime(int(il),int(ay),int(gun))
    t1 = time.mktime(tarix1.timetuple())
    t2 = time.mktime(tarix2.timetuple())

    san = ceil(t2 - t1)
    deq = ceil(san/60)
    saat = ceil(deq/60)
    gun = ceil(saat/24)
    yas = int((tarix1 - tarix2).days / 365)
    print('Siz heyatda'+str(san)+' saniye,'+str(deq)+' deqiqe,'+str(saat)+' saat,'+str(gun)+' gundur ki movcudsunuz')
    print('Sizin '+str(yas)+' yashiniz var')

