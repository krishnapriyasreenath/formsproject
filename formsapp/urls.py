from .import views
from django.urls import path,include

urlpatterns = [
    path('',views.addemp,name="addemp"),
    path('addemploy',views.addemploy,name="addemploy"),
    path('show/',views.show,name="show"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete")

    
]