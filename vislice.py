# datoteka stržnika

import model
import bottle

vislice = model.Vislice()
# id = vislice.nova_igra()

@bottle.get('/')
def indeks():
    return bottle.template('index.tpl')

@bottle.get('/img/<ime>')
def vrni_slike(ime):
    return bottle.static_file(ime, root="img")

@bottle.get('/igra/')
def nova_igra():
    id = vislice.nova_igra()
    bottle.redirect('/igra/{0}/'.format(id))

@bottle.get('/igra/<id:int>/')
def pokazi_igro(id):
    igra, poskus = vislice.igre[id]
    return bottle.template('igra.html', id_igre=id, igra=igra, poskus=poskus)

@bottle.post('/igra/<id:int>/')
def ugibaj(id):
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id, crka)
    bottle.redirect('/igra/{0}/'.format(id))


bottle.run(reloader=True, debug=True)