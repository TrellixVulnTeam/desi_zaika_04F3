from django.shortcuts import render

def index_page(request):
    context = {
        "Heading":"Home"
    }
    return render(request, "Home/index.html", context)


def home_page(request):
    context = {
        "Heading":"Home"
    }
    return render(request, "Home/home.html", context)
