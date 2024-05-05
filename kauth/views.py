from django.shortcuts import render

# Create your views here.




def pagenotfoundView(request, exception):
    return render(request,'web/404.html')

def my_custom_error_view(request):
    return render(request,'web/505.html',status=500)