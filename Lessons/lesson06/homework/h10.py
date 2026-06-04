
'''
🔹 10. Ballar bo‘yicha baho
Vazifa: Foydalanuvchidan imtihon ballini kiriting (0 dan 100 gacha). Quyidagi baholash tizimiga asoslanib, bahoni chiqarilsin:

90-100 — “A”
80-89 — “B”
70-79 — “C”
60-69 — “D”
0-59 — “F”
Test case-lar:

Input	Output
95	A
82	B
75	C
65	D
50	F
'''

ball = int(input("imtihon ballini kiriting: "))
if ball >= 90 and ball <= 100:
    print("A")
elif ball >= 80 and ball <= 89:
    print("B")
elif ball >= 70 and ball <= 79:
    print("C")
elif ball >= 60 and ball <= 69:
    print("D")
elif ball >= 0 and ball <= 59:
    print("F")
else:
    print("Bunday ball mavjud emas!")