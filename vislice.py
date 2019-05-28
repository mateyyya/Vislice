# datoteka stržnika

import model
import bottle

DATOTEKA_STANJA = 'stanje.json'
DATOTEKA_Z_BESEDAMI = 'besede.txt'

vislice = model.Vislice(DATOTEKA_STANJA, DATOTEKA_Z_BESEDAMI)
# id = vislice.nova_igra()

@bottle.get('/')
def indeks():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', str(id_igre), path='/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie('id_igre'))
    igra, poskus = vislice.igre[id_igre]
    return bottle.template('igra.html', id_igre=id_igre, igra=igra, poskus=poskus, model=model)

@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie('id_igre'))
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')

@bottle.get('/img/<ime>')
def vrni_slike(ime):
    return bottle.static_file(ime, root="img")

bottle.run(reloader=True, debug=True)