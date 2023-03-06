from trojkat import Trojkat
from prostokat import Prostokat
from trapez import Trapez
from kolo import  Kolo

tr = Trojkat(5.2,7.8)
print(f'pole figury {tr.__class__.__name__} wynosi: {tr.policz_pole():.2f} cm2')

pr1 = Prostokat(6.7,4.9)
print(f'pole figury {pr1.__class__.__name__} wynosi: {pr1.policz_pole():.2f} cm2')

pr2 = Prostokat(5.2,5.2)
print(f'pole figury {pr2.__class__.__name__} wynosi: {pr2.policz_pole():.2f} cm23')

trp = Trapez(7.6,6.4,4.8)
print(f'pole figury {trp.__class__.__name__} wynosi: {trp.policz_pole():.2f} cm23')


kl = Kolo(5.5)
print(f'pole figury {kl.__class__.__name__} wynosi: {kl.policz_pole():.2f} cm23')
