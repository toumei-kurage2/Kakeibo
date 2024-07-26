from django.urls import path
from . import views
urlpatterns=[
    path("",views.table,name="table"),
    path("register",views.register,name="register"),
    path("list",views.list,name="list"),
    path("update/<int:rireki_id>",views.update,name="update"),
    path("delete/<int:rireki_id>",views.delete,name="delete"),
]
