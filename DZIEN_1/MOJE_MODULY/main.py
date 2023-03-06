# import dane
# import dane as dn
from dane import nfilii as filia
from dane import book as ksiazka
from funkcje.bfunkcje import czytaj_liste,czytaj_dict
from klasy.cdane import CDane

print("___________ wyświetlanie bezpośrednio ________________")
print(filia)
print(ksiazka)

print("___________ wyświetlanie za pomocą funkcji ________________")
czytaj_liste(filia)
czytaj_dict(ksiazka)

print("___________ wyświetlanie za pomocą klasy ________________")
cd = CDane(filia,ksiazka)
cd.czytaj_l()
cd.czytaj_s()
