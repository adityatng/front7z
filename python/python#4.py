'''
#def

def test():
    print('Hello, World!')
test()

def test(f):
    print(f'test {f}..')
test(1)
test(2)
test(3)
test('empat')

def test(f, z):
    print(f'test {f}.. {z}')
test(1,'apa')
test(2,'iya')

def test(f, oke = 1, iya = 2):
    print(f'test fFf {f} xYz {oke} zYx {iya}')
test('[<=f]','[<=oke]', '[<=iya]')

#Rekursif

for i in range(10):
    i += 1
    print(i)

def test(batas, i = 0): 
    print(f'tampilkan {i}')

    if (i < batas): #jika i < batas
        test(batas, i+1) #batas, i ditambah 1 piring
test(5)
'''
