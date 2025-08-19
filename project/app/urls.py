from django.urls import path
from .views import manoj,Sonuview,SonuAdd,SonuGetOne,SonuUpdate,SonuPatch,SonuDelete

urlpatterns = [
    path("",manoj,name="app"),
    path("get/",Sonuview.as_view(),name="get"),
    path("add/",SonuAdd.as_view(),name="add"),
    path("getone/<int:id>/",SonuGetOne.as_view(),name="getone"),
    path("update/<int:id>/",SonuUpdate.as_view(),name="update"),
    path("patch/<int:id>/",SonuPatch.as_view(),name="patch"),
    path("delete/<int:id>/",SonuDelete.as_view(),name="deleted")
]
