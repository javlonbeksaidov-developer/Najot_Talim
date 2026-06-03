
'''
🔹 4. Son ijobiy, manfiy yoki nol
Vazifa: Foydalanuvchidan son kiriting. Agar son > 0 — "Ijobiy son", Agar son < 0 — "Manfiy son", Agar son = 0 — "Nol" deb chiqarilsin.

Test case-lar:

Input	Output
10	Ijobiy son
-5	Manfiy son
0	Nol
'''

son = int(input("Son kiriting: "))
if son > 0:
    print("Ijobiy son")
elif son < 0:
    print("Manfiy son")
else:
    print("Nol")