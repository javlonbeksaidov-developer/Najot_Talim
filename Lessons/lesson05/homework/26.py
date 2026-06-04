
'''
🔹 Task 26: Ekran rejimi yaroqlimi?
Masala: Ekran rejimi "light" yoki "dark" bo‘lishi mumkin. Input: mode (str) Output: True yoki False
'''

mode = input("Ekran rejimi (light/dark): ")
result = mode == "light" or mode == "dark"
print(result)