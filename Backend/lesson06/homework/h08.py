
'''
noto‘g‘ri
🔹 8. Son oraliqda yoki emas
Vazifa: Foydalanuvchidan son kiriting. Agar son 10 dan katta va 100 dan kichik bo‘lsa "Oraliqda" deb chiqarilsin, aks holda "Oraliqda emas".

Test case-lar:

Input	Output
50	Oraliqda
9	Oraliqda emas
101	Oraliqda emas
'''

son = int(input("son kiriting: "))
if son > 10 and son < 100:
    print("Oraliqda")
else:
    print("Oraliqda emas")