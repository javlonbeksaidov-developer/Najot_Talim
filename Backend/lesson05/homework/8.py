
'''
🔹 Task 08: Kirish muvaffaqiyatlimi?
Masala: Login foydalanuvchi nomiga tengmi?

Input: input_username (string), expected_username (string) Output: True yoki False
'''

expected_username = "javlon@gmail.com"
input_username = input("Login: ")

tekshir = input_username == expected_username
print(tekshir)