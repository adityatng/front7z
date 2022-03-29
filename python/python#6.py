from time import strftime
import time, datetime as dt, pyttsx3

#tanngal
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
    if jm == '2345':
        break;
#pyttsx3
f7z = pyttsx3.init()
f7z.say('Happy Birthday')
f7z.runAndWait()
#output
print('\n')
print('='*26)
print('='*6+'happy birthday'+'='*6)
print('='*4+f'{tanggal_lahir}, {tanggal_lahir:%A}'+'='*4)
print('='*3+f'{hari_ini}, {hari_ini:%A}'+'='*3)
print(f'{umur_tahun} tahun, {umur_bulan} bulan, {umur_hari_sisa} hari\n\t\t({umur_hari.days} hari)')
print('='*26)
print(h,'\n')
