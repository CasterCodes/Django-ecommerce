from django.shortcuts import render, redirect
from django.forms import Form
from django.http import HttpResponse
from .models import Products, Category
from django.contrib import messages

# Create your views here.

def index(request):
    products = Products.objects.all();

    return render(request, 'main/home.html', {"products": products})
   
def product_details(request, id):
    product = Products.objects.get(id=id)
    
    return render(request, 'main/product_details.html', {'product': product})
    
def create_product(request):

    if request.method == 'POST':
       if(request.POST.get('save')):  
            product_data = {
                  "name": request.POST.get('product_name'),
                  "category" :request.POST.get('category'),
                  "description" : request.POST.get('description'),
                  "price" : request.POST.get('price'),
                  "image" : request.FILES.get('product_image')
            }

            form = Form(product_data)

            if(form.is_valid()):
                product = Products(name=product_data.get('name'),category=product_data.get('category'),description=product_data.get('description'),price=product_data.get('price'), image=product_data.get('image'))
                product.save()

                messages.info(request=request, extra_tags=messages.SUCCESS, message='Product created successfully')

                
            else:
                messages.info(request=request, extra_tags=messages.ERROR, message='The form data failed validation. Can you please form fields')
                return redirect(to='/create/')

    return render(request, 'main/create_product.html', {} )