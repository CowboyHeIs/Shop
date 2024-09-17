import csv
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from xml.etree.ElementTree import Element, SubElement, tostring
from .forms import ProductForm  # Import ProductForm

def show_main(request):
    products = []
    file_path = os.path.join(os.path.dirname(__file__), 'Products.csv')
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': row.get('id', 'N/A'),
                'product': row.get('products', 'N/A'),
                'price': row.get('price', 'N/A'),
                'desc': row.get('desc', 'N/A'),
            })

    context = {
        'products': products,
        'real_name': 'Heinrich Edric Damadika Suselo',
        'real_class': 'KKI',
        'npm': 2306256356
    }
    return render(request, "main.html", context)

def all_objects_json(request):
    products = []
    file_path = os.path.join(os.path.dirname(__file__), 'Products.csv')
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': row.get('id', 'N/A'),
                'product': row.get('products', 'N/A'),
                'price': row.get('price', 'N/A'),
                'desc': row.get('desc', 'N/A'),
            })
    return JsonResponse(products, safe=False)

def object_by_id_json(request, id):
    products = []
    file_path = os.path.join(os.path.dirname(__file__), 'Products.csv')
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == str(id):
                product = {
                    'id': row.get('id', 'N/A'),
                    'product': row.get('products', 'N/A'),
                    'price': row.get('price', 'N/A'),
                    'desc': row.get('desc', 'N/A'),
                }
                return JsonResponse(product)
    return JsonResponse({'error': 'Product not found'}, status=404)

def all_objects_xml(request):
    products = []
    file_path = os.path.join(os.path.dirname(__file__), 'Products.csv')
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': row.get('id', 'N/A'),
                'product': row.get('products', 'N/A'),
                'price': row.get('price', 'N/A'),
                'desc': row.get('desc', 'N/A'),
            })

    root = Element('products')
    for product in products:
        prod_elem = SubElement(root, 'product')
        for key, value in product.items():
            child = SubElement(prod_elem, key)
            child.text = value

    xml_data = tostring(root, 'utf-8')
    return HttpResponse(xml_data, content_type='application/xml')

def object_by_id_xml(request, id):
    file_path = os.path.join(os.path.dirname(__file__), 'Products.csv')
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == str(id):
                root = Element('product')
                for key, value in row.items():
                    child = SubElement(root, key)
                    child.text = value

                xml_data = tostring(root, 'utf-8')
                return HttpResponse(xml_data, content_type='application/xml')

    return HttpResponse('<error>Product not found</error>', content_type='application/xml', status=404)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')  # Redirect to your main page after saving
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})