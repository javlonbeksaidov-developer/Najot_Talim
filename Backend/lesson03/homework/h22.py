
# 22. QQS bilan mahsulot narxini hisoblash (15%)
# Berilgan: narx = 20000.0 Natija: 23000.0

FOIZ = 15
narx = float(input("Mahsulot narxini kiriting: "))
qqs = narx * (1 + FOIZ /100)
print(f"{FOIZ}% ta'sirida {narx:,.1f} narxdagi mahsulot {qqs} narxga aylandi. ")