
'''
🔹 Task 30: Online, lekin typing emas
Masala: Foydalanuvchi online == True va is_typing == False bo‘lsa. Input: online, is_typing (bool) Output: True yoki False
'''

online = input("Onlinemi? (Ha/Yo'q) ")
is_typing = input("Yozyaptimi? (Ha/Yo'q) ")
result = online == "ha" and is_typing == "yo'q"
print(result)