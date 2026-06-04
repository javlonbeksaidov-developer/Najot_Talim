
'''
🔹 9. Uchburchak turi
Vazifa: Foydalanuvchidan uchta tomon uzunligini kiriting. Ularni asos qilib, uchburchak teng tomonli, teng yonli yoki turli tomonli ekanligini aniqlang.

Test case-lar:

Input	    Output
5, 5, 5	    Teng tomonli
5, 5, 7	    Teng yonli
3, 4, 5	    Turli tomonli
'''

a = int(input("Birinchi tomon uzunligini kiriting: "))
b = int(input("Ikkinchi tomon uzunligini kiriting: "))
c = int(input("Uchinchi tomon uzunligini kiriting: "))

if a == b == c:
    print("uchburchak teng tomonli")
elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print("uchburchak teng yonli")
else:
    print("uchburchak turli tomonli")
