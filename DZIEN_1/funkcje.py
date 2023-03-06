print((lambda g:g**3)(87))

b = lambda a,b,c=1:(a+b)*c

print(b(9,4,2))
print(b(9,4))

def policz(n):
    return lambda a:a*n

print(policz(9)(3))

num = [67,3,-8,3,12,0,99,78,5,17,-99,4,18,8,-11]

parzyste = list(filter(lambda x:x%2==0,num))
print(parzyste)

cube = list(map(lambda x:x**3,num))

print(cube)

#budowa funkcji wyższego rzędu

def witaj(imie):
    return f"Miło Cię widzieć {imie}!"

def konkurs(imie,miasto,punkty):
    return f"Uczestnik konkursu: {imie}, miasto: {miasto}, liczba punktów: {punkty}"


def osoba(funkcja, *args):
    return funkcja(*args)

print(osoba(witaj,"Anna"))
print(osoba(konkurs,"Olga","Kot",88))
