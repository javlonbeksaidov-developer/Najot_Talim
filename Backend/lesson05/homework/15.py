
'''
🔹 Task 15: Foydalanuvchi parolni takrorlay oldimi?
Masala: Parol va parolni tasdiqlash qiymatlari tengmi?

Input: password (string), confirm (string) Output: True yoki False
'''

password = input("Parolni kiriting: ")
confirm = input("Parolni tasdiqlang: ")
result = password == confirm
print(result)