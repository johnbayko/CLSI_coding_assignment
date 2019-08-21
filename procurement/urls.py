from django.urls import path
from procurement.views import ComponentSearchView, DocumentationView
from procurement.api import ComponentAPIList, ComponentAPIRetrieve, Component2APIList, Component2APIRetrieve

urlpatterns = [
    path('', ComponentSearchView.as_view(), name='component-search'),
    path('documentation', DocumentationView.as_view(), name='documentation'),

    # Legacy API Urls
    path('api/components/', ComponentAPIList.as_view(), name='api-component-list'),
    path('api/components/<int:pk>/', ComponentAPIRetrieve.as_view(), name='api-component-retrieve'),

    # API Urls
    path('api/components2/', Component2APIList.as_view(), name='api-component-list'),
    path('api/components2/<int:pk>/', Component2APIRetrieve.as_view(), name='api-component-retrieve'),
]
