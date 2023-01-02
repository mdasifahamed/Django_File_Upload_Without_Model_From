from django.urls import path
from UploadFile import views


urlpatterns =[
    path("",views.home, name="home"),
    path("uploads/",views.uploads, name= "uploads"),
    path("all_data/",views.all_data, name="all_data"),

    path("id/",views.id, name ='id'),
    path("delete/",views.delete, name='delete'),
    path("search/",views.search, name= 'search'),
    path("update/",views.update, name="update"),
    path("delete_photo_temp/",views.delete_photo_temp,name="delete_photo_temp"),
    path("updated/",views.updated,name="updated"),
    path("delete/",views.delete,name = 'delete'),
    path("delete_profile_temp/",views.delete_profile_temp,name="delete_profile_temp"),
    path("delete_profile/",views.delete_profile,name="delete_profile")
]