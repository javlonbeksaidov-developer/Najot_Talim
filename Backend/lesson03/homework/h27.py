
#27. Pulni to‘lov birliklariga ajratish
#Berilgan: pul = 38500 Natija: “3 dona 10000 so‘mlik, 1 dona 5000 so‘mlik, 1 dona 2000 so‘mlik, 3 dona 500 so‘mlik”

pul = int(input("Pul miqdorini kiriting: "))
birliklar = [10000, 5000, 2000, 500]
a = pul // 10000                                # 10000 so‘mliklar soni
b = (pul % 10000) // 5000                       # 5000 so‘mliklar soni
c = ((pul % 10000) % 5000) // 2000              # 2000 so‘mliklar soni
d = (((pul % 10000) % 5000) % 2000) // 500      # 500 so‘mliklar soni
print(f"{pul} so‘mlik {a} dona 10000 so‘mlik, {b} dona 5000 so‘mlik, {c} dona 2000 so‘mlik, {d} dona 500 so‘mlikdan iborat.")
