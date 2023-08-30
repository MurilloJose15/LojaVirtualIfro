from django.urls import reverse_lazy
from django.views.generic import FormView, View
from loja.models import Produto
from .carrinho import Carinnho
from .forms import CarrinhoAddProdutoForm


class CarrinhoAdd(FormView):
    form_class = CarrinhoAddProdutoForm
    sucess_url =reverse_lazy('carrinhodetlhe')

    def post(self, request, *args, **kwargs):
        self.produto = Produto.objects.get(id=kwargs['idprod'])
        