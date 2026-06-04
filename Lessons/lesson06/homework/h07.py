
'''
🔹 7. Email manzilini tekshirish
Vazifa: Foydalanuvchidan email manzilini kiriting. Email manzili quyidagi shartlarni qanoatlantirishi kerak:

@ belgisi bo‘lishi
@ dan keyin nuqta (.) bo‘lishi
Bo‘sh joy bo‘lmasligi
Agar shartlar bajarilsa — "Email manzili to‘g‘ri", aks holda "Email manzili noto‘g‘ri" deb chiqarilsin.

Test case-lar:

Input	Output
user@example.com	Email manzili to‘g‘ri
userexample.com	Email manzili noto‘g‘ri
user@ex ample.com	Email manzili noto‘g‘ri
user@examplecom	Email manzili noto‘g‘ri
'''

email = input("email manzilini kiriting: ")
if ("@" in email) and (".com" in email) and (" " not in email):
    print("to‘g‘ri")
else:
    print("noto‘g‘ri")