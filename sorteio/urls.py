from django.conf.urls import url, include

from .views import (
   DezenasMaisSorteadas, DezenasMenosSorteadas
)

urlpatterns = [
    url(r'^mais-sorteadas/$',
        DezenasMaisSorteadas.as_view(),
        name='mais-sorteadas'),
    url(r'^menos-sorteadas/$',
        DezenasMenosSorteadas.as_view(),
        name='menos-sorteadas'),
    # url(r'^atualizar-camada/(?P<pk>\w+)$',
    #     GeoserverLayersUpdateView.as_view(),
    #     name='geoserver-layers-update'),
    # url(r'^deletar-camada/(?P<pk>\w+)$',
    #     GeoserverLayersDeleteView.as_view(),
    #     name='geoserver-layers-delete'),

    # url(r'^listar-abas/$',
    #     TabLayersListView.as_view(),
    #     name='tab-layers-list'),
    # url(r'^registrar-aba/$',
    #     TabLayersRegisterView.as_view(),
    #     name='tab-layers-register'),
    # url(r'^atualizar-aba/(?P<pk>\w+)$',
    #     TabLayersUpdateView.as_view(),
    #     name='tab-layers-update'),
    # url(r'^deletar-aba/(?P<pk>\w+)$',
    #     TabLayersDeleteView.as_view(),
    #     name='tab-layers-delete'),

    # url(r'^user/$',
    #     UserListView.as_view(),
    #     name='users-list-create'),
    # url(r'^user-delete/(?P<pk>\w+)$',
    #     UserDeleteView.as_view(),
    #     name='users-delete'),

]