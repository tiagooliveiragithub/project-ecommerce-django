from produto.models import Produto, Variacao
from django.contrib import admin


class VariacaoInline(admin.TabularInline):
    model = Variacao
    min_num = 1
    extra = 0
    can_delete = True


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta',
                    'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [
        VariacaoInline
    ]
