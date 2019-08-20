from django.urls import path
from procurement.views import ComponentSearchView, DocumentationView
#from procurement.api import ComponentAPIList, ComponentAPIRetrieve
from procurement.api import ComponentAPIList, ComponentAPIRetrieve, Component2APIList, Component2APIRetrieve, RepresentativeAPIList, SupplierAPIList

urlpatterns = [
    path('', ComponentSearchView.as_view(), name='component-search'),
    path('documentation', DocumentationView.as_view(), name='documentation'),

    # API Urls
    path('api/components/', ComponentAPIList.as_view(), name='api-component-list'),
    path('api/components/<int:pk>/', ComponentAPIRetrieve.as_view(), name='api-component-retrieve'),

    path('api/components2/', Component2APIList.as_view(), name='api-component-list'),
    path('api/components2/<int:pk>/', Component2APIRetrieve.as_view(), name='api-component-retrieve'),

    # debug
    path('api/representatives/', RepresentativeAPIList.as_view(), name='api-representative-list'),
    path('api/suppliers/', SupplierAPIList.as_view(), name='api-representative-list'),
]
