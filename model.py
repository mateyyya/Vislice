import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZACETEK = 'S'
ZMAGA = 'W'
PORAZ = 'X'

with open('besede.txt') as f:
    bazen_besed = [beseda.strip() for beseda in f.readlines()]

class Igra:
    def __init__(self, geslo):
        self.geslo = geslo.upper()
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
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        # return "".join(c if c in self.crke else '_' for c in selg.geslo)
        novi = ''
        for c in self.geslo:
            if c in self.crke:
                novi += c
            else:
                novi += '_'
            novi += ' '
        return novi

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        if crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            return PRAVILNA_CRKA
        # potem je napačna neponovljena
        self.crke.append(crka)
        if self.poraz():
            return PORAZ
        else:
            return NAPACNA_CRKA

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)

class Vislice:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        return len(self.igre)

    def nova_igra(self):
        id = self.prost_id_igre()
        self.igre[id] = (nova_igra(), ZACETEK)
        return id

    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, poskus)
    



v = Vislice()
v.nova_igra()
v.nova_igra()
print(v.igre)


# print(bazen_besed[0])
# print(bazen_besed[-1])


# igra = Igra("nekaj")
# igra.crke = ['A', 'L', 'V', 'N', 'X', 'E']
# print(igra.napacne_crke())
# print(igra.pravilne_crke())
# print(igra.stevilo_napak())
# print(igra.zmaga())
# print(igra.poraz())
# print(igra.pravilni_del_gesla())
# print(igra.nepravili_ugibi())
# print("ugibam k")
# print(igra.ugibaj('k'))
# print(igra.pravilni_del_gesla())
# print(igra.nepravili_ugibi())
# print("ugibam v")
# print(igra.ugibaj('v'))
# print(igra.pravilni_del_gesla())
# print(igra.nepravili_ugibi())
# print("ugibam f")
# print(igra.ugibaj('f'))