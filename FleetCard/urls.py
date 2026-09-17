from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contatos/', views.contatos, name='contatos'),
    path('pagina_veiculos/', views.pagina_veiculos, name='pagina_veiculos'),
    path("pagina_veiculos/detalhes/<str:tipo>/<str:marca>/<str:modelo>/", views.ver_detalhes, name="ver_detalhes"),
    path('deslogar/', views.deslogar, name='deslogar'),

    #crud corpo site
    path('veiculos/', views.lista_veiculos, name='lista_veiculos'),
    path("veiculos/cadastrar/", views.cadastrar_veiculo, name="cadastrar_veiculo"),
    path("veiculos/editar/<int:id>/", views.editar_veiculo, name="editar_veiculo"),
    path("veiculos/excluir/<int:id>/", views.excluir_veiculo, name="excluir_veiculo"),
]