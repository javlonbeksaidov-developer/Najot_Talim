
'''
🔹 Task 27: Mahsulot mavjud yoki kutilmoqda
Masala: Mahsulot in_stock yoki on_delivery bo‘lsa, mavjud hisoblanadi. Input: in_stock, on_delivery (bool) Output: True yoki False
'''

in_stock = input("Mahsulot omborda bormi? (Ha/Yo'q) ")
on_delivery = input("Mahsulot omborda bormi? (Ha/Yo'q) ")
result = in_stock == "ha" or on_delivery == "ha"
print(result)