
'''
🔹 Task 19: Kabisa yili
Masala: Berilgan yil kabisa yili ekanligini aniqlang.

Input: year (int) Output: True yoki False
'''

year = int(input("Yilni kiriting: "))
result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(result)