import random
import json

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZACETEK = 'S'
ZMAGA = 'W'
PORAZ = 'X'

DATOTEKA_S_STANJEM = 'stanje.json'
DATOTEKA_Z_BESEDAMI = 'besede.txt'

# with open('besede.txt') as f:
#     bazen_besed = [beseda.strip() for beseda in f.readlines()]

class Igra:
    def __init__(self, geslo, crke=[]):
        self.geslo = geslo.upper()
        self.crke = crke

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



class Vislice:
    def __init__(self, datoteka_s_stanjem, datoteka_z_besedami):
        self.igre = {}
        self.datoteka_z_besedami = datoteka_z_besedami
        self.datoteka_s_stanjem = datoteka_s_stanjem
        with open(self.datoteka_z_besedami, encoding='utf-8') as datoteka_z_besedami:
            self.bazen_besed = [vrstica.strip().upper() for vrstica in datoteka_z_besedami.readlines()]
        self.nalozi_igre_iz_datoteke()

    def prost_id_igre(self):
        return len(self.igre)

    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        igra = Igra(random.choice(self.bazen_besed))
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return id_igre

    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        igra, _ = self.igre[id_igre]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, poskus)
        self.zapisi_igre_v_datoteko()

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w') as f:
            igre = {str(id_igre): {'poskus': poskus, 'geslo': igra.geslo, 'crke': igra.crke} for id_igre, (igra, poskus) in self.igre.items()}
            json.dump(igre, f)

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as f:
            igre = json.loads(f.read())
            self.igre = {}
            for id_igre, opis_igre in igre.items():
                self.igre[int(id_igre)] = (Igra(opis_igre['geslo'], crke=opis_igre['crke']), opis_igre['poskus'])
    



# v = Vislice()
# v.nova_igra()
# v.nova_igra()
# print(v.igre)


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