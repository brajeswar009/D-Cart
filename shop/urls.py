from django.urls import path
from shop import views 

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker', views.tracker, name="Tracking"),
    path('search/', views.search, name="Search"),
    path('notfound/', views.notfound, name="Notfound"),
    path('products/<int:myid>', views.pView, name="ProductView"),
    path('checkout/', views.checkout, name="CheckOut"),
]
