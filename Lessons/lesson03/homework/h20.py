
# 20. Oylik foiz bilan yillik pul miqdorini hisoblash
# Berilgan: oylik = 1000000.0, foiz = 12 Natija: 1120000.0

oylik = float(input("Oylik maoshingizni kiriting: "))
foiz = float(input("foiz miqdorini kiriting: "))
yillik = oylik * (1 + foiz / 100)
print(f"Oylik {oylik:,.1f}, foiz {foiz} bo'lganda, natija {yillik:,.1f}ga teng bo'ladi.")
