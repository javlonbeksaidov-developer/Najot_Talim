
'''
3. average_spending_tracker.py – Kartadagi o‘rtacha harajatlar
Vazifa:
Haftalik xarajatlaringizni 7 ta qiymat sifatida kiriting. Masalan: 12.0, 15.0, 10.0, 13.0, 12.5, 11.0, 14.0.

Dastur quyidagilarni bajaradi:

Haftalik xarajatlarning o‘rtachasini hisoblab, ikki o‘nlikdan iborat qiymatni chiqaradi.
Natijani raqam va so‘z shaklida (ingliz va rus tillarida) chiqarilsin.
Misol:

Haftalik harajatlarni kiriting: 12.0, 15.0, 10.0, 13.0, 12.5, 11.0, 14.0
O‘rtacha harajat: $12.64 (twelve dollars and sixty-four cents, двенадцать долларов шестьдесят четыре цента)
'''

from num2words import num2words

monday = float(input("Dushanba kunining xarajatini kiriting: "))
tuesday = float(input("Seshanba kunining xarajatini kiriting: "))
wednesday = float(input("Chorshanba kunining xarajatini kiriting: "))
thursday = float(input("Payshanba kunining xarajatini kiriting: "))
friday = float(input("Juma kunining xarajatini kiriting: "))
saturday = float(input("Shanba kunining xarajatini kiriting: "))
sunday = float(input("Yakshanba kunining xarajatini kiriting: "))

total = monday + tuesday + wednesday + thursday + friday + saturday + sunday
average = total / 7

print(
    f"Haftalik xarajatlar: {total:.2f} so'm",
    num2words(total, to='currency'),
    num2words(total, lang='ru', to='currency'),
)

print(
        f"O'rta xarajat: {average:.2f} so'm",
    num2words(average, to='currency'),
    num2words(average, lang='ru', to='currency')
)
