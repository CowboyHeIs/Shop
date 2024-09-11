import csv
from django.shortcuts import render
import os

def show_main(request):
    products = []
    file_path = os.path.join(os.path.dirname(__file__),'Products.csv')
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'product': row.get('products', 'N/A'),
                'price': row.get('price', 'N/A'),
                'desc': row.get('desc', 'N/A')
            })

    context = {
        'products': products,
        'real_name' : 'Heinrich Edric Damadika Suselo',
        'real_class' : 'KKI',
        'npm' : 2306256356
    }

    return render(request, "main.html", context)
