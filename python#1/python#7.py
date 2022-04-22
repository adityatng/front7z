#day7/100daysofpython
#autotyping

import pyautogui as f7z
import time

'''
time.sleep(2)
while True:
    f7z.typewrite("test")
    f7z.press("enter")
    time.sleep(2)
'''
time.sleep(2)
total=0
for i in range(10): #total ketikan
    total+=1 #hitungan ketikan +1
    f7z.typewrite(f"test {total}")
    f7z.press("enter")
    time.sleep(1) #waktu jeda/detik
else:
    print("Selesai..") #ketika selesai
