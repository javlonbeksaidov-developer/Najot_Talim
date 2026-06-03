
'''
🔹 3. Harf katta yoki kichik
Vazifa: Foydalanuvchidan bitta harf kiriting. Agar harf katta bo‘lsa "Katta harf", kichik bo‘lsa "Kichik harf" deb chiqarilsin.

Test case-lar:

Input	    Output
A	    Katta harf
z	    Kichik harf
G	    Katta harf
'''

harf = input("Harf kiriting: ")
if harf.isupper():
    print("Katta harf")
elif harf.islower():
    print("Kichik harf")
else:
    print("Iltimos, bitta harf kiriting.")