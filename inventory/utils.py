from django.utils import timezone

for product in Product.objects.all():
    product.expired = product.expiry_date <= timezone.now().date()
    product.save()
