
'''
🔹 Task 39: Ism bosh harfi katta emas
Masala: Foydalanuvchi ismi bosh harfi katta bo‘lmasa, False. Input: name (str) Output: True yoki False
'''

name = input("Ismingizni kiriting: ")
first_letter = name[0]
result = first_letter.isupper()
print(result)