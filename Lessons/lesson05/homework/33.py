
'''
🔹 Task 33: Foydalanuvchi faqat login qilgan (admin emas)
Masala: logged_in == True, lekin is_admin == False bo‘lsa. Input: logged_in, is_admin (bool) Output: True yoki False
'''

logged_in = input("login qilganmi? (Ha/Yo'q) ")
is_admin = input("Adminmi? (Ha/Yo'q) ")
result = logged_in == "ha" and is_admin == "yo'q"
print(result)