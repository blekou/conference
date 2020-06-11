from django.shortcuts import render

def index(request):
    datas = {

    }
    return render(request, 'pages/index.html',datas)


def about(request):
    datas = {

    }
    return render(request, 'pages/about.html',datas)


def contact(request):
    datas = {

    }
    return render(request, 'pages/contact.html',datas)
