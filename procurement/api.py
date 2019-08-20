from rest_framework.generics import ListAPIView, RetrieveAPIView

#from procurement.models import Component
from procurement.models import Component, Representative, Supplier
#from procurement.serializers import ComponentSerializer, Component2Serializer
from procurement.serializers import ComponentSerializer, Component2Serializer, Representative2Serializer, Supplier2Serializer


class ComponentAPIList(ListAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class ComponentAPIRetrieve(RetrieveAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class Component2APIList(ListAPIView):
    queryset = Component.objects.all()
    serializer_class = Component2Serializer


class Component2APIRetrieve(RetrieveAPIView):
    queryset = Component.objects.all()
    serializer_class = Component2Serializer


#debiug
class RepresentativeAPIList(ListAPIView):
    queryset = Representative.objects.all()
    serializer_class = Representative2Serializer

class SupplierAPIList(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = Supplier2Serializer
