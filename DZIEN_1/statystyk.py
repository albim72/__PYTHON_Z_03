liczby = [56,1009,-999,0,12,56,199,-99,145,677,333,-876,177,833,101]

def pokaz_statystyki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum-minimum
    liczba_el = len(lista)
    suma_el = sum(lista)
    srednia_arytm = suma_el/liczba_el
    return minimum, maksimum, rozstep, liczba_el,suma_el,srednia_arytm

wynik = pokaz_statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,lel,suma_el,sred_ar = pokaz_statystyki(liczby)
print(f"wartość największa: {maxi}, wartość najmniejsza: {mini}, rozstęp: {roz}, liczba elemenetów: {lel},"
      f" suma elementów: {suma_el}, średnia arytmetyczna: {sred_ar}")
