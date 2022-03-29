from tkinter import*
from tkinter.ttk import*
from time import strftime

root = Tk()
root.title('clock')

def time():
    string = strftime('%H:%M:%S %P')
    lbl.config(text = string)
    lbl.after(1000, time)
print(strftime('%H:%M:%S %P'))
lbl = Label(root, font = ('calibri', 40, 'bold'),
background = 'purple',
foreground = 'white')

lbl.pack(anchor = 'center')
time()
mainloop()






from time import strftime
import time, datetime, pyttsx3

dt = datetime.datetime.now()
f7z = pyttsx3.init()
while True:
    y = dt.year
    m = dt.month
    d = dt.day
    j = strftime('%H')
    mn = strftime('%M')
    dk = strftime('%S %P')

    print(f'{d}/{m}/{y} {j}:{mn}:{dk}')
    f7z.say(f'{d}/{m}/{y} {j}:{mn}:{dk}')
    f7z.runAndWait()
    time.sleep(5)
    if j == '22' and mn == '07':
        print('='*26)
        print(f'== happy birthday ==\n{d}/{m}/{y} {j}:{mn}:{dk}')
        print('='*26)
        f7z.say(f'happy birthday')
        f7z.runAndWait()
        break;



from time import strftime
import time, datetime as dt, pyttsx3

tahun = 2000
bulan = 3
tanggal = 26

tanggal_lahir = dt.date(tahun,bulan,tanggal)
hari_ini = dt.date.today()

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
umur_hari_sisa = tanggal - umur_bulan
#loop
while True:
    h = strftime('%Y/%m/%d %H:%M:%S %P')
    jm = strftime('%H%M')
    print(h)
    time.sleep(5)
    if jm == '2314':
        break;
#pyttsx3
f7z = pyttsx3.init()
f7z.say(f'happy birthday')
f7z.runAndWait()
print('='*26)
print('='*6+'happy birthday'+'='*6)
print('='*4+f'{tanggal_lahir}, {tanggal_lahir:%A}'+'='*4)
print('='*4+f'{hari_ini}, {hari_ini:%A}'+'='*4)
print(f'{umur_tahun} tahun, {umur_bulan} bulan, {umur_hari_sisa} hari \n\t\t({umur_hari.days} hari)')
print('='*26)