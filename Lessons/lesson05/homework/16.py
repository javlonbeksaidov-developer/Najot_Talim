
'''
🔹 Task 16: Foydalanuvchi to‘liq login qilganmi?
Masala: Login va parol ikkalasi ham bo‘sh bo‘lmasligi kerak.

Input: login (string), password (string) Output: True yoki False
'''

login = input("Login kiriting: ")
password = input("password kiriting: ")

a = len(login)
b = len(password)
result = a and b != 0
print(result)