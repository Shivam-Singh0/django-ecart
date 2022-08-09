from django.shortcuts import redirect, render


from shop.models import Order, Products
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_objects = Products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name:
        product_objects = Products.objects.filter(title__icontains=item_name)
    
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    return render(request, 'shop/index.html', {'product_objects':product_objects})



def detail(request, item_id):
    product_object = Products.objects.get(id=item_id)
    return render(request, 'shop/detail.html', {'product_object':product_object})


def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        
        address = request.POST.get('address', "")
        zip = request.POST.get('zip', "")
        total = request.POST.get('total', "")

        order = Order(items=items, name=name, email=email, address=address, zip=zip, total=total)
        order.save()
        return redirect('/')
    return render(request, 'shop/checkout.html')