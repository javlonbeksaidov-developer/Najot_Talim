
'''
🔹 Task 24: Foydalanuvchi admin va tizimga kirganmi?
Masala: Foydalanuvchi admin bo‘lishi va tizimga kirgan bo‘lishi kerak. Input: is_admin (bool), is_logged_in (bool) Output: True yoki False
'''

is_admin = input("Adminmisiz? (Ha/Yo'q) ")
is_logged_in = input("Login qilinganmi? (Ha/Yo'q) ")

result = (is_admin == "ha") and (is_logged_in == "ha")
print(result)