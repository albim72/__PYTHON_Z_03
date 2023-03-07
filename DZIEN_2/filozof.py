odp = input("Czy Ziemia jest płaska?Czy chcesz znać odpowiedź? (t/n): ")
if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self):
    return "Tak! Ziemia jest płaska!"

def nowaodpowiedz(self):
    return "Nie! Ziemia jest elipsoidą!"

def brak(self):
    return "nie, to nie... brak odpowiedzi!"

class SednoOdpowiedzi(type):
    def __init__(cls,clsname,bases,attribs):
        if required:
            if attribs.get('cn'):
                cls.odpowiedz = nowaodpowiedz
            else:
                cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak


class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

class Kopernik(metaclass=SednoOdpowiedzi):
    cn = True

class Einstein(metaclass=SednoOdpowiedzi):
    cn = True

fil1 = Arystoteles()
print(f"filozof {fil1.__class__.__name__} mówi: {fil1.odpowiedz()}")

fil2 = Platon()
print(f"filozof {fil2.__class__.__name__} mówi: {fil2.odpowiedz()}")

fil3 = SwTomasz()
print(f"filozof {fil3.__class__.__name__} mówi: {fil3.odpowiedz()}")

fil4 = Kopernik()
print(f"filozof {fil4.__class__.__name__} mówi: {fil4.odpowiedz()}")

fil5 = Einstein()
print(f"filozof {fil5.__class__.__name__} mówi: {fil5.odpowiedz()}")
