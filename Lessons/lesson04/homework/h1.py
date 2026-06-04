
'''
1. cash_denomination_splitter.py – Kupyuraga ajratish (pulni kupyuralarga ajratish)
Vazifa:
Sizga $da pul miqdori beriladi. Masalan, foydalanuvchi 186 dollarni kiritsa, uni $50, $10, $5, va $1 kupyuralariga ajratish kerak. Dastur har bir kupyuradan nechta ekanligini aniq hisoblab, natijani shunday ko‘rinishda chiqarsin:

Masalan:

Pul miqdorini kiriting ($): 186
$50 kupyuradan: 3 ta
$10 kupyuradan: 3 ta
$5 kupyuradan: 1 ta
$1 kupyuradan: 1 ta
Umumiy summa: $186 (one hundred and eighty-six, сто восемьдесят шесть)
'''

from num2words import num2words

price = int(input("Narxni kiriting: "))
birliklar = [50, 10, 5, 1]

price_50 = price // 50
print(f"50 birlikdan {price_50} ta bor")

price_10 = (price - price_50 * 50) // 10
print(f"10 birlikdan {price_10} ta bor")

price_5 = (price - price_50 * 50 - price_10 * 10) // 5
print(f"5 birlikdan {price_5} ta bor")

price_1 = (price - price_50 * 50 - price_10 * 10 - price_5 * 5)
print(f"1 birlikdan {price_1} ta bor")

print(
    price,
    num2words(price),
    num2words(price, lang="ru")
)