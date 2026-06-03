
'''
🔹 1. Son juft yoki toqligini aniqlash
Vazifa: Foydalanuvchidan son kiriting. Agar son 2 ga bo‘linganda qoldiq 0 bo‘lsa, "Juft son", aks holda "Toq son" deb chiqarilsin.

Test case-lar:

Input	    Output
10	    Juft son
7	    Toq son
0	    Juft son
'''

son = int(input("Istalgan son kiriting: "))
if son % 2 == 0:
    print("Juft son")
else:
    print("Toq son")
    