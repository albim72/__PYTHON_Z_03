#n!=1*2*3...*n -> niezdefiniowana dla n<0
#double 1.8E+308
#n?? -> 171

import sys
from silniaerror import SilniaErr

sys.set_int_max_str_digits(0x100000)
sys.setrecursionlimit(0x1000000)
def silnia(n):
    if n < 0:
        raise SilniaErr(n)
    wynik=1
    for i in range(1,n+1):
        wynik*=i
    return wynik

def silnia_rek(n):
    if n < 0:
        raise SilniaErr(n)
    if n == 0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj wartość atrybutu n funckji silnia: "))
    print(f"silnia z {n} wynosi: {silnia(n)}")
    print(f"silnia rekurencyjna z {n} wynosi: {silnia_rek(n)}")
except SilniaErr as se:
    print(se)
