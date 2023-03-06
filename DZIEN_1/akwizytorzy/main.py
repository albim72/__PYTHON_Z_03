from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class Szef:
    def __repr__(self):
        return 'jestem szefem wszytkich szefów....'

    def zarobek(self):
        return Decimal('12_000_000.00')

k = Szef()

a = Akwizytor("Jan","Kot",5245435,Decimal('167899.00'),Decimal('7.35'))

h = AkwizytorNaEtacie("Olga","Kos",7565456,Decimal('154300'),Decimal('5.23'),Decimal('4500'))

pracownicy = [a,h,k]

for prac in pracownicy:
    print(prac)
    print(f'{prac.zarobek():,.2f} zł\n')
