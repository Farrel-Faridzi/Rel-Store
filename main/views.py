from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406436240',
        'name': 'Farrel Faridzi Liwungang',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)