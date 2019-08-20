from django.contrib import admin
from django.shortcuts import render_to_response, get_object_or_404

from procurement.admin_forms import ComponentAdminForm
from procurement.models import Supplier, Representative, Component


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_authorized', 'updated')
    filter_horizonal = ('components',)


class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('representative_name', 'representative_email', 'updated')


class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'updated')
    form = ComponentAdminForm
    source_components_template = 'procurement/admin_templates/source_components.html'

    def source_components(self, request, pk):
        component = get_object_or_404(Component, pk=pk)

        return render_to_response(self.source_components_template, {
            'title': 'Source Suppliers for: %s' % component,
            'opts': self.model._meta,
            'component': component,
            'supplier_results': component.suppliers.filter(is_authorized=True),

        })


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Representative, RepresentativeAdmin)
admin.site.register(Component, ComponentAdmin)
