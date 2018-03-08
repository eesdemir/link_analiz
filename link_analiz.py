# -*- coding: utf-8 -*-

import requests
baglanti = requests.get('http://csgoarenasi')
deger=baglanti.status_code
if (deger/100==2):

    print'baglanti basarili :',deger
elif (deger/100==4):
    print'baglanti basarisiz :', deger
