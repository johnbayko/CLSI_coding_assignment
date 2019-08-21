from rest_framework.generics import ListAPIView, RetrieveAPIView

from procurement.models import Component, Representative, Supplier
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
