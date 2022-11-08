from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("aboutus/",views.about,name="abtus"),
    path("form/",views.form,name="fm"),
    path("delete/<int:id>",views.delete_data,name="del"),
    path("update/<int:id>",views.update_data,name="update"),
]