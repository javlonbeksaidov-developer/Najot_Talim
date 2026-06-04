
'''
🔹 Task 31: Foydalanuvchi erkak yoki yoshi katta
Masala: Gender male yoki yoshi 60 dan katta bo‘lsa. Input: gender (str), age (int) Output: True yoki False
'''

gender = input("Jinsingiz? (ayol/erkak) ")
age = int(input("Yoshingiz nechida? "))
result = gender == "erkak" or age >= 60
print(result)