from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
# from .forms import UserRegisterForm, InventoryItemForm

# Create your views herd


def testview(request):
    return render(request, 'inventory/index.html')

@login_required
def dashboard(request):
    items = Product.objects.all()

    context = {
            'items': items,
          }
    return render(request, 'inventory/dashboard.html', context)

