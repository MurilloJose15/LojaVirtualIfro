from django.urls import path
from loja import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('produtos', views.ProdutoListView.as_view(), name='listarprod'),
    path('<slug:categ_slug>', views.ProdutoListView.as_view(), name='listarprodcateg'),
    path('produto/<pk>/<slug>', views.ProdutoDetailView.as_view(), name='detalheprod'),
<<<<<<< HEAD
]
=======
]
>>>>>>> 3c654bf01c0ab15178f44122bd795ed619b16dc8
