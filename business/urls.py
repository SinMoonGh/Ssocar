from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:customer_id>", views.customer_detail, name="detail"),
]