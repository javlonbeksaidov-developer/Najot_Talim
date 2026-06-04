
'''
5. delivery_service_price.py – Yetkazib berish xizmati narxi
Vazifa:
Yetkazib berish narxi:

Boshlang‘ich to‘lov: $5.00
Har 1 km uchun: $0.80
Foydalanuvchi masofani kiritadi. Dastur umumiy narxni hisoblab, raqam va so‘zda (ingliz va rus) chiqaradi.

Misol:

Masofani kiriting (km): 3.5
Yetkazib berish narxi: $7.80 (seven dollars and eighty cents, семь долларов восемьдесят центов)
'''

from num2words import num2words

masofa = float(input("Masofani kiriting (km): "))
boshlangich_tolov = 5.00
km_tolov = 0.80

total_price = boshlangich_tolov + masofa * km_tolov

print(
    f"Yetkazib berish narxi: {total_price:.2f}",
    num2words(total_price, to='currency'),
    num2words(total_price, to='currency', lang = "ru")
)