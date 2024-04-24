from django.contrib import admin

from .models import eggsInventory

# Register your models here.

class EggsInventoryAdmin(admin.ModelAdmin):

    # Define a custom form for the admin interface

    def get_form(self, request, obj=None, **kwargs):

        form = super().get_form(request, obj, **kwargs)

        # Customize the location field to use a dropdown menu

        form.base_fields['location'].widget.can_add_related = False

        form.base_fields['location'].widget.can_change_related = False

        form.base_fields['location'].widget.can_delete_related = False

        return form



admin.site.register( eggsInventory, EggsInventoryAdmin)