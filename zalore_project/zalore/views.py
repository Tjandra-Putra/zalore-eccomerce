from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import Support, Product  #.models means in the model file in current package
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages

def home(request):
    return render(request, 'zalore/index.html')


def cart(request):
    return render(request, 'zalore/cart.html')


def clothing(request):
    context = {
        'product_data': Product.objects.all()
    }
    return render(request, 'zalore/clothing.html', context)


class ClothingDetailView(DetailView):
    model = Product
    print(model.product_name)
    # This expects html format as <modelName>_<view_type>.html


def support(request):
    if request.method == "POST":
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        object_support = Support(first_name=firstName, last_name=lastName, email=email, message=message)
        object_support.save()

        messages.add_message(request, messages.SUCCESS, "Enquiry has been submitted successfully.")

    return render(request, 'zalore/support.html')


def admin_support(request):
    context = {
        'support_data': Support.objects.filter()  # HTML takes key from dictionary
    }
    return render(request, 'zalore/admin/admin_support.html', context)


def admin_dashboard(request):
    return render(request, 'zalore/admin/admin_dashboard.html')


def admin_product(request):
    if request.method == "POST":
        name = request.POST.get('product_name')
        description = request.POST.get('product_description')
        price = request.POST.get('product_price')
        discount = request.POST.get('product_discount')
        stock = request.POST.get('product_stock')
        image = request.FILES['product_image']

        fs = FileSystemStorage()  #defaults to   MEDIA_ROOT
        filename = fs.save(image.name, image)  # saves the file to `media` folder
        uploaded_file_url = fs.url(filename)  # gets the url

        print("FIRST" + uploaded_file_url)  #/media/nike_2.jpg
        print("SECOND" + filename)  #nike_2.jpg

        obj = Product(product_name=name, product_description=description, product_price=price, product_discount=discount, product_stock=stock, product_image=filename)
        obj.save()

        messages.add_message(request, messages.SUCCESS, "Product has been listed.")


    context = {
        'product_data': Product.objects.all()
    }

    return render(request, 'zalore/admin/admin_product.html', context)

def admin_product_delete(request, id):
    object = Product.objects.get(pk=id)
    object.delete()

    fs = FileSystemStorage()  # defaults to   MEDIA_ROOT
    fs.delete(str(object.product_image))

    messages.add_message(request, messages.SUCCESS, '"{}" has been deleted.'.format(object.product_name))

    return redirect('/admin/product')


