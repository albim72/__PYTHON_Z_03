from ipojazd import IPojazd

class Pojazd(IPojazd):

    def spalanie(self, odl, litry):
        return litry*100/odl

    def kosztyprzejazdu(self, odl, litry, cena_l):
        return self.spalanie(odl,litry)*(odl/100)*cena_l

    def opis(self, msg):
        return f"spalanie {msg}:"

    def multipojazd(self, odl, litry, msg):
        return super().multipojazd(odl, litry, msg)

