
'''
4-Vazifa:
Taxi narxi quyidagicha hisoblanadi:

Boshlang‘ich to‘lov: $3.00
Har 1 km uchun: $1.20
Foydalanuvchi masofani km da kiritadi (masalan: 5.2).

Dastur yakuniy to‘lovni hisoblab, ikki o‘nlikka yaxlitlab chiqaradi. Natijani ham raqam, ham so‘z shaklida (ingliz va rus tillarida) chiqarsin.

Misol:

Masofani kiriting (km): 5.2
Taxi narxi: $9.24 (nine dollars and twenty-four cents, девять долларов двадцать четыре цента)
'''

from num2words import num2words

masofa = float(input("Masofani kiriting (km): "))
boshlangich_tolov = 3.00
km_tolov = 1.20

total_tolov = boshlangich_tolov + (masofa * km_tolov)
rounded_tolov = round(total_tolov, 2)

print(
    f"Taxi narxi: ${rounded_tolov:.2f}",
    num2words(rounded_tolov, to='currency'),
    num2words(rounded_tolov, lang='ru', to='currency'),
)