
'''
🔹 12. Parollar mos keladimi?
Vazifa: Foydalanuvchidan ikki marta parol kiriting. Agar parollar bir xil bo‘lsa “Parol qabul qilindi”, aks holda “Parollar mos emas” deb chiqarilsin.

Test case-lar:

Input	    Output
“abc123”,   “abc123”	Parol qabul qilindi
“12345”,    “54321”	    Parollar mos emas
'''

parol = input("Parol kiriting: ")
tasdiq = input("Parolni qayta kiriting: ")

if parol == tasdiq:
    print("Parol qabul qilindi")
else:
    print("Parollar mos emas")