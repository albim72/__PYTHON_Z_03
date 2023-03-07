from pojazd import Pojazd

p1 = Pojazd()
odl = 567
litry = 46
cn = 7.12
print(f"{p1.spalanie(odl,litry):.2f}")
print(f"{p1.kosztyprzejazdu(odl,litry,cn):.2f}")
print(p1.opis("[l/100km]"))
print(p1.multipojazd(189,16," l/100km "))
