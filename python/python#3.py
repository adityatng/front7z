'''
#1format
print('Hello, {wrld}'.format(wrld='World!'))
#2PercabanganIf-Else-Elif
nilai = 85
print('Nilai Anda Adalah: ', nilai,'\n')
if nilai >=70:
    print('Selamat, anda lulus!')
else:
    print('Maaf, anda tidak lulus.')
if nilai >= 90:
        print('predikat A')
elif nilai >= 80:
        print('predikat B')
elif nilai >= 70:
        print('predikat C')
elif nilai >= 60:
        print('predikat D')
else:
        print('predikat E')


#3PerulanganFor
nilai_angka = 75
batas_nilai = [100,80,70,65,60,50,40,0]
nilai_abjad = ['A', 'AB', 'B', 'BC', 'C', 'D', 'E', ]

for i in range(7):
    if nilai_angka <= batas_nilai[i] and nilai_angka > batas_nilai[i+1]:
        print('index nilai: ', nilai_abjad[i])


1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

for i in range(5):
    print()
    for x in range(5):
        print(x+1, end=' ')


#4PerulanganWhile
i = 1
while i <= 5:
    i += 1
    print(i)
while True:
    print('y')
    break;


#perulanganBersarangWhile
max_baris = 7
max_kolom = 5

baris = 0
while baris < max_baris:
    kolom = 0
    while kolom < max_kolom:
        print('o' if kolom <= baris else '+', end = ' ')
        kolom += 1
    else:
        print('')
        baris += 1



i = 31
while i <= 125:
    i += 1
    print(f'{i} [%c]'%i)
    

    '''

