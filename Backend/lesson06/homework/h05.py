
'''
🔹 5. Bank omonati foizlari
Vazifa: Foydalanuvchidan omonat summasini kiriting. Agar omonat summasi:

100000 so‘mdan kam bo‘lsa: foiz 5%
100000 - 500000 so‘m oralig‘ida bo‘lsa: foiz 7%
500000 so‘mdan katta bo‘lsa: foiz 10%
Test case-lar:

Input	Output
50000	5%
100000	7%
300000	7%
600000	10%
99999	5%
'''

omonat_sum = int(input("Omonat summasini kiriting: "))
if omonat_sum < 100_000:
    print("5%")
elif omonat_sum >= 100_000 and omonat_sum < 500_000:
    print("7%")
else:
    print("10%")