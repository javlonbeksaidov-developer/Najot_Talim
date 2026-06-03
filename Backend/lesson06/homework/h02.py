
'''
🔹 2. Kattaroq sonni toping
Vazifa: Foydalanuvchidan ikki son kiriting. Kattaroq sonni chiqarilsin.

Test case-lar:

Input	    Output
5 va 10	    10
20 va 15	20
7 va 7	    Teng
'''

first_digit = int(input("Birinchi raqamni kiriting: "))
second_digit = int(input("Ikkinchi raqamni kiriting: "))

if first_digit == second_digit:
    print("Teng")
elif first_digit > second_digit:
    print(f"{first_digit}")
else:
    print(f"{second_digit}")