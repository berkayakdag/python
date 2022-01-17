#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:34:33 2021

@author: berkayakdag
"""

biber_köz = False
biber = False
et = 100
et_sıcaklığı = 0
kıyma = 0
tuz_miktarı = 0
kekik_miktarı = 0
while True:

    veri = input("> ").lower()

    if veri == "bıçak":
        sayı = int(input("Kaça bölüceksin > "))
        print("Eti",sayı,"parçaya böldün")
        et = et / sayı
    
    elif veri == "kıyma_makinesi":
     kıyma = et
     et = 0

    
    elif veri == "et":
        print(et)
    
    elif veri == "+kekik":
        kekik_miktarı = kekik_miktarı + 5
        print("Ete kekik attın")
        
    elif veri == "+tuz":
        tuz_miktarı = tuz_miktarı + 5
        print("Eti tuzladın")
    elif tuz_miktarı > 40:
        print("çok tuzladın")
        
    elif veri == "tuz":
        print(tuz_miktarı)
        
    elif veri == "kekik":
        print(kekik_miktarı)
        
    elif veri == "sıcaklık":
        print(et_sıcaklığı,"derece")
        
    elif veri == "rehber":
        print("""Bıçak - eti böler
              kıyma_makinesi - kıyma yapar
              et - et miktarını gösterir
              +kekik - kekik ekler
              +tuz - tuz ekler
              tuz - tuz miktarını gösterir
              kekik - kekik miktarını gösterir
              sıcaklık - et sıcaklığı miktarını gösterir
              kıyma - kıyma miktarını gösterir
              tava - yemeği pişirir
              
              """)
              
    elif veri == "biber":
        biber = True
        print("biber ekledin")
        
    elif veri == "közle":
     neyi_közleyeceksin = input("neyi közleyeceksin")
     if neyi_közleyeceksin == "biber":
         biber_köz = True
         print("biberi közledin")
         
    
    elif veri == "kıyma":
        print(kıyma)
        
    elif veri == "tava": 
        et_saniyesi = int(input("Kaç saniye pişireceksin > "))
        et_sıcaklığı = et_saniyesi * 5
        if et_saniyesi < 100:
            print("az pişmiş")
        elif et_saniyesi > 100 and et_saniyesi < 500:
            print("orta pişmiş")
        else: 
            print("çok pişmiş")
                    
    elif veri == "bitti":   
        if biber_köz == True and et_sıcaklığı > 50:
            print("bişeyler")
    
        
    elif veri == "çık":
        break