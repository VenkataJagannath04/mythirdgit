from django.shortcuts import render

# Create your views here.
def Jinja_print(request):
    d={'Name': 'Ruparaju Venkata Jagannadha Rama Seshu Sharma'}
    return render(request, 'Jinja_print.html', context=d)
