from ipojazd import IPojazd

class Pojazd(IPojazd):

    def spalanie(self, odl, litry):
        return litry*100/odl

    def kosztyprzejazdu(self, odl, litry, cena_l):
        return self.spalanie(litry,odl)*(odl/100)*cena_l

    def opis(self, msg):
        return "spalanie [l/100km]:"

    def multipojazd(self):
        return super().multipojazd()
