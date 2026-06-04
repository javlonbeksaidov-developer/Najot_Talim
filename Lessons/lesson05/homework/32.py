
'''
Task 32: Harorat xavfli emas
Masala: Harorat 37.5 dan past yoki 42 dan katta bo‘lmasa, xavfli emas. Input: temperature (float) Output: True yoki False
'''

temperature = float(input("Haroratni kiriting: "))
result = (temperature >= 37.5) and (temperature <= 42)
print(result)