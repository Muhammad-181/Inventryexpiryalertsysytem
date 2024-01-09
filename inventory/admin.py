from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import Staff, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = (
                        'expired',
                        'product_name',
                        'production_date',
                        'date_recieved',
                        'Price',
                        'expiry_date',
                    )
    search_fields = (
                        'expired',
                        'product_name',
                        'production_date',
                        'date_recieved',
                        'Price',
                        'expiry_date',
                        )
    list_display = (
                    'product_name',
                    'date_recieved',
                    'expiry_date',
                    'expired',
                    'Price',
                    )
    def download_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="selected_items.csv"'

        writer = csv.writer(response)
        # Assuming YourModel has fields 'field1', 'field2', 'field3'...
        fields = ['product_name', 'product_quantity', 'date_recieved', 'production_date', 'expiry_date']  # Replace with your model's fields
        writer.writerow(fields)

        for obj in queryset:
            row = [getattr(obj, field) for field in fields]
            writer.writerow(row)

        return response
    download_as_csv.short_description = "Download selected items as CSV"
    actions = [download_as_csv]

admin.site.register(Staff)
admin.site.register(Product, ProductAdmin)
