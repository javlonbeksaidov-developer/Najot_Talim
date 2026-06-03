
'''
🔹 Task 40: Kiritilgan PIN to‘g‘ri emas va 4 xonali emas
Masala: PIN to‘g‘ri bo‘lmasligi yoki uzunligi 4 ga teng emasligi. Input: pin (str), correct_pin (str) Output: True yoki False
'''

correct_pin = "123456"
pin = input("Pin kiriting: ")
pin_len = len(pin)
result = (pin != correct_pin) and (pin_len != 4)
print(result)