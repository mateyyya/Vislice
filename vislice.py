# datoteka stržnika

import model
import bottle

vislice = model.Vislice()
id = vislice.nova_igra()
igra, poskus = vislice.igre[id]

@bottle.get('/')
def indeks():
    return bottle.template('index.tpl')

@bottle.get('/img/<ime>')
def vrni_slike(ime):
    return bottle.static_file(ime, root="img")

@bottle.get('/igra/')
def igratest():
    return bottle.template('igra.html', id_igre=id, igra=igra, poskus=poskus)


bottle.run(reloader=True, debug=True)