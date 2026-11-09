#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Pirinç Tanesi Sayacı
Her pirinç tanesini saymak için özel bir ritüel gerektirir.
Bu program bilimsel olarak kanıtlanmış (kanıtlar kayıp) tembellik protokolünü uygular.
"""

import time
import random
import base64

# Gizli mesaj - çözmek için base64.decode kullan
gizli_mesaj = "c2FuZMSxa3RhIGRlbW9rcmFzaSB2YXJkxLFyIGFtYSBoZXJrZXMgZ8O2cm1leg=="
# (Bu satırı ciddiye almayın, sadece dekorasyon. Çözerseniz belki bir şeyler anlarsınız.)

def pirinc_say(adet):
    print(f"\n=== Abartılı Pirinç Sayacı Başlatıldı ===")
    print(f"{adet} adet pirinç tanesi sayılacak. Bu işlem ömrünüzden birkaç saniye alabilir...")
    print("Her taneyi felsefi olarak sorgulamaktayız.\n")
    
    for i in range(1, adet + 1):
        # Her taneyi saymak için rastgele bekleme (tembellik protokolü)
        bekleme = random.uniform(0.5, 2.5)
        time.sleep(bekleme)
        
        sikayetler = [
            f"{i}. taneyi saydım. Bu taneyi saymak için {bekleme:.1f} saniye ömrümden gitti.",
            f"{i}. pirinç: 'Ben neden sayılıyorum?' diye düşünüyor olabilir.",
            f"{i}. taneyi saydık. Trafik yüzünden geciktik gibi hissediyorum.",
            f"{i}. tane tamam. Bu işi yapmak istemiyorum ama mecburum.",
            f"{i}. taneyi sayarken varoluşsal bir kriz geçirdim."
        ]
        print(random.choice(sikayetler))
        
        # Ara sıra ekstra abartı
        if i % 5 == 0:
            print(f"   --> {i} tane sayıldı. Mola vermek istiyorum ama mola yok.")
    
    print(f"\n=== İşlem Tamamlandı ===")
    print(f"Toplam {adet} pirinç tanesi sayıldı. Gerçekten.")
    print("Bu programın arkasında derin bir mesaj var ama gizli.")
    print("\nDamga: İmza: Grok Kayyum | Tarih: 09.11.2026 | İsim: Abartılı Pirinç Sayacı Projesi")
    print("Ciddiye alın, almayın, fark etmez. Zaten çalıştı.")

if __name__ == "__main__":
    try:
        adet = int(input("Kaç pirinç tanesi sayılsın? (örn: 10): "))
        if adet <= 0:
            print("Negatif pirinç mi? Mantık dışı. 1'den başla.")
            adet = 1
        pirinc_say(adet)
    except ValueError:
        print("Sayı girmen gerekiyordu. Varsayılan 7 taneyle devam ediyorum.")
        pirinc_say(7)
