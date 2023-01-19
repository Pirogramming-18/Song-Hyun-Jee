from django.urls import path
from . import views


app_name = "posts"

urlpatterns = [
    path("", views.site_main, name="main"),
    path("posts/idcreate", views.site_idcreate, name="idcreate"),
    path("posts/<int:pk>", views.site_iddetail, name="iddetail"),
    path("posts/<int:pk>/idupdate", views.site_idupdate, name="idupdate"),
    path("posts/<int:pk>/iddelete", views.site_iddelete, name="iddelete"),
    path("posts/devlist", views.site_devlist, name="devlist"),
    path("posts/devcreate", views.site_devcreate, name="devcreate"),
    path("posts/devdetail/<int:pk>", views.site_devdetail, name="devdetail"),
    path("posts/<int:pk>/devupdate", views.site_devupdate, name="devupdate"),
    path("posts/<int:pk>/devdelete", views.site_devdelete, name="devdelete"),
]
