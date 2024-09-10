from django.shortcuts import render

def show_main(request):
    context = {
        'price' : '23.000,00',
        'product': 'Bintang 0,0%',
        'desc': 'Non-alcoholic'
    }

    return render(request, "main.html", context)