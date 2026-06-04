
'''
🔹 Task 28: Parol noto‘g‘ri yoki bo‘sh
Masala: Parol "" yoki secret ga teng bo‘lmasa – xatolik. Input: password (str) Output: True yoki False
'''

secret = "hello"
password = input("Parol: ")
result = password != "" or password != secret
print(result)