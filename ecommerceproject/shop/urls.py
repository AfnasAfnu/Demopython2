from django.urls import path
from . import views
app_name='shop'
urlpatterns = [

    # path('',views.index,name='index')
    path('', views.allproductCat, name='allproductCat'),
    path('<slug:c_slug>/',views.allproductCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),

]