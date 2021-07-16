from django.shortcuts import render


def post_login(request):
    return render(request, 'blog/post_login.html', {})

def post_menu(request):
    return render(request, 'blog/post_menu.html', {})

def post_menu_cliente(request):
    return render(request, 'blog/post_menu_cliente.html', {})
# Create your views here.
