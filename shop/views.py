from django.shortcuts import render
from django.template import loader
from .models import ShopModels


def main(req):
    template = loader.get_template('shop/main.html')
    return render(req, 'shop/main.html')


def catalog(req):
    template = loader.get_template('shop/catalog.html')

    succulent = ShopModels.objects.get(name='Листовые суккуленты')
    exotic = ShopModels.objects.get(name='Антуриум ДАКОТА')
    cashpo = ShopModels.objects.get(name='Горшок/кашпо')
    flying = ShopModels.objects.get(name='Летающее растение')
    palma = ShopModels.objects.get(name='Комнатная пальма')

    context = {'succulent': succulent, 'exotic': exotic, 'cashpo': cashpo, 'flying': flying, 'palma': palma}

    return render(req, 'shop/catalog.html', context)


def delivery(req):
    template = loader.get_template('shop/delivery.html')
    return render(req, 'shop/delivery.html')


def contacts(req):
    template = loader.get_template('shop/delivery.html')
    return render(req, 'shop/contacts.html')
