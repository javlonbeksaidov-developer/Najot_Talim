
'''
🔹 Task 36: Avtomatik yangilanish faqat light modeda
Masala: Agar auto_update == True va mode == "light" bo‘lsa, ishlasin. Input: auto_update (bool), mode (str) Output: True yoki False
'''

auto_update = input("Avtomatik yangilanish yoniqmi? (Ha/Yo'q) ")
mode = input("'light' mode yoniqmi? (Ha/Yo'q) ")
result = (auto_update == "ha") and (mode == "ha")
print(result)