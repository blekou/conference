from django.shortcuts import render

def speakers(request):
    datas = {

    }
    return render(request, 'pages/speakers.html',datas)


def tickets(request):
    datas = {

    }
    return render(request, 'pages/tickets.html',datas)



def schedule(request):
    datas = {

    }
    return render(request, 'pages/schedule.html',datas)
