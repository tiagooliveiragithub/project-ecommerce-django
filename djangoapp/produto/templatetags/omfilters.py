from django.template import Library
from utils import preco


register = Library()


@register.filter
def formata_preco(val):
    return preco.formata_preco(val)


@register.filter
def cart_total_qtd(carrinho):
    return preco.cart_total_qtd(carrinho)


@register.filter
def cart_totals(carrinho):
    return preco.cart_totals(carrinho)
