from rest_framework import serializers
from procurement.models import Component, Supplier, Representative


class SupplierSerializer(serializers.ModelSerializer):
    representative_name = serializers.SerializerMethodField()
    representative_email = serializers.SerializerMethodField()

    class Meta:
        model = Supplier
        exclude = ('created', 'updated')

    def get_representative_name(self, obj):
        return obj.representatives.order_by('id').first().representative_name

    def get_representative_email(self, obj):
        return obj.representatives.order_by('id').first().representative_email


class ComponentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(source='__str__', read_only=True)
    suppliers = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = Component
        exclude = ('created', 'updated')


class Representative2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Representative
        exclude = ('created', 'updated')


class Supplier2Serializer(serializers.ModelSerializer):
    representatives = Representative2Serializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        exclude = ('created', 'updated')


class Component2Serializer(serializers.ModelSerializer):
    text = serializers.CharField(source='__str__', read_only=True)
    suppliers = Supplier2Serializer(many=True, read_only=True)

    class Meta:
        model = Component
        exclude = ('created', 'updated')


