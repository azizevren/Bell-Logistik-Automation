import datetime

def baslik_yazdir():
    tarih = datetime.datetime.now().strftime("%d.%m.%Y")
    print("="*40)
    print(f" BELL BASEL - LAGER & PREIS TOOL")
    print(f" Datum: {tarih}")
    print("="*40 +"\n")

def kdv_hesapla(fiyat):
    """Fiyata %8.1 Isvicre KDV'si ekler"""
    return round(fiyat * 1.081, 2)

def stok_kontrol(urunler):
    """Kritik stok seviyesindeki ürünleri bulur"""
    print("--- KRITISCHE LAGERBESTÄNDE ---")
    alarm_var = False

    for urun in urunler:
        if urun["stok"] < 50:
            alarm_var = True
            print(f"🚨 Achtung: {urun['ad']} (Bestand: {urun['stok']} kg/Stk)")

    if not alarm_var:
        print("✅ Alles im grünen Bereich.")
    print("-"*30)

def fiyat_listesi_olustur(urunler):
    """Zamli ve KDV'li yeni fiyat listesini basar"""
    print("\n--- NEUE PREISLISTE (inkl. 8.1% MwSt) ---")

    for urun in urunler:
        ham_fiyat = urun["fiyat"]
        zamli_fiyat = ham_fiyat * 1.20
        satis_fiyati = kdv_hesapla(zamli_fiyat)

        print(f"📦 {urun['ad']}")
        print(f" Alte Preis: {ham_fiyat} CHF")
        print(f" Neue Preis: {satis_fiyati} CHF (inkl. MwSt)")
        print("-" * 30)

depo_urunleri = [
    {"ad": "Bell Würste (Klassik)", "stok": 450, "fiyat": 5.50},
    {"ad":"Rindfleisch (bio)", "stok": 30, "fiyat": 42.00},
    {"ad":"Pouletburst", "stok": 120, "fiyat": 18.00},
    {"ad":"Grillsaucen Mix", "stok": 15, "fiyat": 3.20}
]
baslik_yazdir()
stok_kontrol(depo_urunleri)
fiyat_listesi_olustur(depo_urunleri)