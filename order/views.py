from django.shortcuts import render

def order_index(request):
    """
    Function of displaying the home page of the site.
    """
    return render(request,'main.html')