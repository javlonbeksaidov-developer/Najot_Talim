
# 23. Bankdagi pulni yillik foiz bilan hisoblash
# Berilgan: pul = 500000.0, foiz = 10 Natija: 550000.0

FOIZ = 10
pul = float(input("Bankdan olgan summangizni kiriting: "))
natija = pul * (1 + FOIZ / 100)
print(f"{pul} miqdordagi pul {FOIZ}%da 1 yilda {natija} bo'ladi. ")