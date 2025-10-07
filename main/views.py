from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    category_filter = request.GET.get("category", None)

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    if category_filter:
        product_list = product_list.filter(category=category_filter)

    product_categories = Product.CATEGORY_CHOICES

    context = {
        'npm': '2406436240',
        'name': 'Farrel Faridzi Liwungang',
        'class': 'PBP D',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'product_categories': product_categories,
    }
    return render(request, "main.html", context)



@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return JsonResponse({
                "status": "success",
                "pk": product_entry.pk,
                "fields": {
                    "name": product_entry.name,
                    "price": product_entry.price,
                    "description": product_entry.description,
                    "image": product_entry.image,
                    "category": product_entry.category,
                    "views": product_entry.views,
                }
            }, status=201)
        else:
            return JsonResponse({
                "status": "error", 
                "errors": form.errors.as_json() # Gunakan .as_json() untuk detail
            }, status=400)


    form = ProductForm()
    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    products_list = Product.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    category = request.GET.get('category', None)
    
    products_list = Product.objects.all()
    if category:
        products_list = products_list.filter(category=category)
    
    json_data = serializers.serialize("json", products_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
        

def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
    
def register(request):
    if request.method == 'POST':
        # Cek apakah ini request AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = json.loads(request.body)
            form = UserCreationForm(data)
        else:
            form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            # Untuk AJAX, kembalikan JSON
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success', 'message': 'Account created successfully! Please login.'})
            # Untuk non-AJAX, lakukan redirect
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            # Untuk AJAX, kembalikan error sebagai JSON
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Mengambil error dan memformatnya agar mudah dibaca
                errors = {field: [e for e in error] for field, error in form.errors.items()}
                return JsonResponse({'status': 'error', 'errors': errors}, status=400)
    
    # Untuk request GET, tampilkan halaman register seperti biasa
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        # Cek apakah ini request AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = json.loads(request.body)
            form = AuthenticationForm(request, data=data)
        else:
            form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Untuk AJAX, kembalikan JSON
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success', 'message': 'Login successful!'})
            # Untuk non-AJAX, lakukan redirect seperti biasa
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            # Untuk AJAX, kembalikan error sebagai JSON
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    
    # Untuk request GET, tampilkan halaman login seperti biasa
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        # Proses update data
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Product updated successfully.'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()}, status=400)
    
    # Bagian ini tetap untuk render halaman jika diakses via GET
    form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def delete_product_ajax(request, id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(pk=id)
            product.delete()
            return JsonResponse({'status': 'success', 'message': 'Product deleted successfully.'})
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Product not found.'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)