
'''
🔹 11. Yilning faslini aniqlash
Vazifa: Foydalanuvchidan oy raqamini (1 dan 12 gacha) kiriting. Oyga qarab faslni aniqlang:

12, 1, 2 — Qish
3, 4, 5 — Bahor
6, 7, 8 — Yoz
9, 10, 11 — Kuz
Test case-lar:

Input	Output
1	Qish
4	Bahor
7	Yoz
10	Kuz
'''

oy = int(input("Oy raqamini (1 dan 12 gacha) kiriting: "))
if oy == 12 or oy == 1 or oy == 2:
    print("Qish faslining oyi")
elif oy == 3 or oy == 4 or oy == 5:
    print("Bahor faslining oyi")
elif oy == 6 or oy == 7 or oy == 8:
    print("Yoz faslining oyi")
elif oy == 9 or oy == 10 or oy == 11:
    print("Kuz faslining oyi")
else:
    print("Xato son kiritdingiz! (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) ")