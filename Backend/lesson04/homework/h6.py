
'''
6. electricity_bill_calculator.py – Elektr energiyasi hisoblash
Vazifa:
Foydalanuvchi oy boshidagi va oy oxiridagi hisoblagich ko‘rsatkichlarini kiritadi (kWh).

Narx: 1 kWh = $0.45

Dastur to‘lovni hisoblab chiqadi, ikki o‘nlikka yaxlitlaydi va natijani raqam va so‘z shaklida (ingliz va rus) chiqaradi.

Misol:

Oy boshidagi ko‘rsatkich: 1234.5
Oy oxiridagi ko‘rsatkich: 1300.75
To‘lov: $29.42 (twenty-nine dollars and forty-two cents, двадцать девять долларов сорок два цента)
'''

from num2words import num2words

oy_start = float(input("Oy boshidagi ko‘rsatkich:"))
oy_finish = float(input("Oy oxiridagi ko‘rsatkich:"))
elektr = 0.45

total = (oy_finish - oy_start) * elektr

print(
    f"To‘lov: {total:.2f}",
    num2words(total, to = 'currency'),
    num2words(total, to = "currency", lang = "ru")
)