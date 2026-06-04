
'''
🔹 Task 38: Sessiya aktiv emas
Masala: logged_in == False yoki session_time == 0 bo‘lsa. Input: logged_in (bool), session_time (int) Output: True yoki False
'''

logged_in = input("Sessiya mavjudmi? (Ha/Yo'q) ")
session_time = int(input("Tugashiga qancha vaqt qoldi? "))
result = (logged_in == "yo'q") or (session_time == 0)
print(result)