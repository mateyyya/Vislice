STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo):
        self.geslo = geslo
        self.crke = []

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all(c in self.crke for c in self.geslo)
    
    def poraz(self):
        pass



igra = Igra("nekaj")
igra.crke = ['a', 'l', 'v', 'n', 'x', 'e', 'k', 'j']
print(igra.napacne_crke())
print(igra.pravilne_crke())
print(igra.stevilo_napak())
print(igra.zmaga())
print(igra.poraz())