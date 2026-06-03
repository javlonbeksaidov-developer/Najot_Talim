
'''
2. fast_food_price_rounder.py – Fast-food narx kalkulyatori
Vazifa:
Foydalanuvchi fast-food mahsulotlarining narxlarini kiritadi (masalan: 4.5, 3.2, 5.5). Dastur quyidagilarni bajarsin:

Narxlarni jamlab hisoblasin.
Yakuniy summani eng yaqin 0.1 dollarga yaxlitlab chiqarsin.
Natijani raqam va so‘z shaklida (ingliz va rus tillarida) chiqarsin.
Masalan:

Mahsulot narxlarini kiriting: 4.5, 3.2, 5.5
Umumiy narx: $13.20 (thirteen dollars and twenty cents, тринадцать долларов двадцать центов)
Yaxlitlangan narx: $13.20 (thirteen dollars and twenty cents, тринадцать долларов двадцать центов)
'''

from num2words import num2words

price1 = float(input("Birinchi mahsulot narxini kiriting: "))
price2 = float(input("Ikkinchi mahsulot narxini kiriting: "))
price3 = float(input("Uchinchi mahsulot narxini kiriting: "))

total_price = price1 + price2 + price3
rounded_price = round(total_price, 1)

print(
    f"Umumiy narx: ${total_price:.2f}",
    num2words(total_price, to='currency'),
    num2words(total_price, lang='ru', to='currency'),
)

print(
    f"Yaxlitlangan narx: ${rounded_price:.2f}",
    num2words(rounded_price, to='currency'),
    num2words(rounded_price, lang='ru', to='currency'),
)