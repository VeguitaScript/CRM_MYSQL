from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.client.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.product.views import *
from core.erp.views.op_comercial.views import *

app_name = 'erp'

urlpatterns = [
    #Categoria
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    # producto
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # cliente
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    # oportunidad comercial
    path('op_comercial/list/', OpComercialListView.as_view(), name='op_comercial_list'),
    path('op_comercial/add/', OpComercialCreateView.as_view(), name='op_comercial_create'),
    path('op_comercial/update/<int:pk>/', OpComercialUpdateView.as_view(), name='op_comercial_update'),
    path('op_comercial/delete/<int:pk>/', OpComercialDeleteView.as_view(), name='op_comercial_delete'),

    #Home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

]        