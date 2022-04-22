import pyautogui as f7z
import datetime as dt
import time

'''
#tanpa batas
time.sleep(2)
while True:
    f7z.typewrite('test')
    f7z.press('enter')
    time.sleep(1)
    print(dt.datetime.now())
'''

#mengunakan jumlah yang diinginkan
#range(10)(total ketikan)
#timesleep(jeda/detik)

total=0
time.sleep(2)
for i in range(10):
    total+=1
    f7z.typewrite(f'woi..! {total}')
    f7z.press('enter')
    time.sleep(1)
    print(dt.datetime.now())
else:
    print('Selesai..')
