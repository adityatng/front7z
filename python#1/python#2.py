#day2/100daysofpython
#datetime

import datetime as dt

hari_ini = dt.date.today()
print(f"Hari ini : {hari_ini}, {hari_ini:%A}")

#tanggal lahir
tahun = 2000
bulan = 3
tanggal = 26

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir: {tanggal_lahir}, {tanggal_lahir:%A}")

umur_hari = hari_ini - tanggal_lahir
print(umur_hari)
umur_tahun = umur_hari.days // 365
print(umur_tahun)
umur_bulan = (umur_hari.days % 365) // 30
print(umur_bulan)
umur_hari_sisa = tanggal - umur_bulan
print(umur_hari_sisa)

print(f"Umur anda adalah : {umur_tahun} tahun, {umur_bulan} bulan, {umur_hari_sisa} hari")
print(f"Anda telah hidup dibumi selama: {umur_hari.days} hari ")

