
import model

# če je v isti mapi, končnica .py tako uvoziš vse funkcije iz tiste datoteke

def izpis_igre(igra):
    tekst = """
Število preostalih poskusov: {0}
{1}
Napačne črke ({2}): {3}
    """.format(
        model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        igra.pravilni_del_gesla(),
        igra.stevilo_napak(),
        igra.nepravili_ugibi()
    )
    return tekst

def izpis_zmage(igra):
    tekst = """
###### BRAVO! Uganil si geslo '{0}' ######
    """.format(
        igra.geslo
    )
    return tekst

def izpis_poraza(igra):
    tekst = """
!!!!!! JOOOOJ! Porabil si vse poskuse. Geslo je '{0}' !!!!!!
    """.format(
        igra.geslo
    )
    return tekst

def zahtevaj_vnos():
    return input("Vnesi črko: ")

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        if len(crka) != 1:
            print("Ne me *****!!")
            continue
        rez = igra.ugibaj(crka)
        if rez == model.ZMAGA:
            print(izpis_zmage(igra))
            return
        if rez == model.PORAZ:
            print(izpis_poraza(igra))
            return

pozeni_vmesnik()
# igra = model.nova_igra()
# print(izpis_igre(igra))
# print(izpis_zmage(igra))
# print(izpis_poraza(igra))
