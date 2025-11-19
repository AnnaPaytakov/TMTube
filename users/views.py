from django.shortcuts import render

#! CBV gecmeli
def register(request):
    return render(request, "users/register.html")