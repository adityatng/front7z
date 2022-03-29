#FibonacciNonRekursif
'''
panjang = 10
fibo = [0,1]

for i in range(2,panjang):
    a1 = fibo[i - 2]
    a2 = fibo[i - 1]
    ags = a1 + a2
    fibo.append(ags) 
    print(fibo)

for i in range(panjang):
    if (i < 2):
        print(i)
    else:
        index1 = i - 2
        index2 = i - 1
        print(f'Penjumlahan dari index-{index1} dan index-{index2}')

#fibonacciDenganRekursif

def fibonacci(n):
    return [n]
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))

def fibonacci (n):
    if n < 1:
        return [n]

    lsn = fibonacci(n - 1)
    a1 = lsn[-2] if len(lsn) > 2 else 0
    a2 = lsn[-1] if len(lsn) > 1 else 1
    print('lsn', lsn)
    print(f'{a1}, {a2}')

    return lsn + [a1 + a2]

print(fibonacci(5))

'''
aList = [5,10,15,25]
print(aList[::-2])