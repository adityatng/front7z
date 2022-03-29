#operator Aritmatika

a, b = 6, 4
'''
print(a, '+', b, '=', a+b)
print(a, '-', b, '=', a-b)
print(a, '*', b, '=', a*b)
print(a, '/', b, '=', a/b)
print(a, '%', b, '=', a%b)
print(a, '**', b, '=', a**b)
print(a, '//', b, '=', a//b)


#operasi Komparasi atau Perbandingan

print(a, '>', b, '=', a>b)
print(a, '<', b, '=', a<b)
print(a, '==', b, '=', a==b)
print(a, '!=', b, '=', a!=b)
print(a, '>=', b, '=', a>=b)
print(a, '<=', b, '=', a<=b)

'''
#Operator Penugasan

a = 10
print('a = 10 ->', a)
a += 5
print('a += 5 ->', a)
a -= 3
print('a -= 3 ->', a)
a *= 6
print('a *= 6 ->', a)
a /= 9
print('a /= 9 ->', a)
b %= 90
print('b %= 90 ->', b)


#Operator Logika

print(True and True)
print(1 + 2 == 3 and True)
print('----')
print(False or 1 > 5)
print(False or 5 > 2)
print('----')
print(not(1 > 5))
print(not(1 < 5))

#Operator Keanggotaan

perusahaan = 'Front7z'
list_pulau = ['sumut', 'sulawesi']
mahasiswa ={
    'nama': 'Front7z',
    'asal': 'sumut'
}

print("apakah 'c' ada di variabel perusahaan?", 'c' in perusahaan)

