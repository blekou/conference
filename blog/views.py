from django.shortcuts import render

def blog(request):
    datas = {

    }
    return render(request, 'pages/blog.html',datas)


def single(request):
    datas = {

    }
    return render(request, 'pages/single-blog.html',datas)
