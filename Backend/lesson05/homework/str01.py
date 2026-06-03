
'''
1. Telefon raqamni formatlash
Foydalanuvchi quyidagi formatda telefon raqam kiritadi: 971234567 Siz bu raqamni quyidagi formatga o‘zgartiruvchi dastur yozing: +998 97 123 45 67
'''

tel_raqam = input("Telefon raqamingizni kiriting: 9ta raqam (991234567)": )
tel_1 = tel_raqam[0:2]
tel_2 = tel_raqam[2:5]
tel_3 = tel_raqam[5:7]
tel_4 = tel_raqam[7:9]
uzb_raqam = "+998" + " " + tel_1 + " " + tel_2 + " " + tel_3 + " " + tel_4
print(uzb_raqam)

print(f"Telefon raqamingiz: +998 {tel_1} {tel_2} {tel_3} {tel_4}")