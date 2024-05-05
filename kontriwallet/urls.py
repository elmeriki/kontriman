from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    # path('', include('administrator.urls')),
    # path('', include('kauth.urls')),
]

handler404 ='kauth.views.pagenotfoundView'
handler500 = 'kauth.views.my_custom_error_view'