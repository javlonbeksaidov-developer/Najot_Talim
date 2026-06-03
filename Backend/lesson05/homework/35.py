
'''
🔹 Task 35: Foydalanuvchi yozayotgan, lekin noaniq
Masala: is_typing == True va username == "" bo‘lsa, noaniq foydalanuvchi yozmoqda. Input: is_typing (bool), username (str) Output: True yoki False
'''

is_typing = input("Yozayaptimi? (Ha/Yo'q) ")
username = input("Foydalanuvchi nomi: ")
result = (is_typing == "ha") and (username == "")
print(result)