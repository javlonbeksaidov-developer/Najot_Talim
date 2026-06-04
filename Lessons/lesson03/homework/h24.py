
# 24. Chegirma bilan mahsulot narxi
# Berilgan: narx = 500000.0, chegirma = 10 Natija: 450000.0

CHEGIRMA = 10
narx = float(input("Mahsulot narxini kiriting: "))
natija = narx * (1 - CHEGIRMA / 100)
print(f"Siz kiritgan {narx} narxli mahsulot {CHEGIRMA}% asosida {natija}ga aylanib qolibdi. ")