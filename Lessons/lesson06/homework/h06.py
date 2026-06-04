
'''
🔹 6. Telefon raqami operatorini aniqlash
Vazifa: Foydalanuvchidan telefon raqamini kiriting (masalan: 90xxxxxxx). Raqam boshidagi kodga qarab operatorni aniqlang:

90, 91 — Ucell
93, 94 — Beeline
95, 97 — Uzmobile
88, 99 — Mobiuz
Boshqalar — noma’lum operator
Test case-lar:

Input	Output
909876543	Ucell
931234567	Beeline
959876543	Uzmobile
881234567	Mobiuz
921234567	Noma’lum operator
'''

tel_raqam = int(input("telefon raqamini kiriting: (masalan: 90xxxxxxx) "))
kod_raqam = tel_raqam // 10_000_000
print(f"+998 {tel_raqam}")
print(f"{kod_raqam}")

if kod_raqam == 90 or kod_raqam == 91:
    print("Ucell")
elif kod_raqam == 93 or kod_raqam == 94:
    print("Beeline")
elif kod_raqam == 95 or kod_raqam == 97:
    print("Uzmobile")
elif kod_raqam == 88 or kod_raqam == 99:
    print("Mobiuz")
else:
    print("Nomalum operator")