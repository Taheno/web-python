
from django.contrib import admin
from django.urls import path, include, re_path
from app.views import data_atual
from app.views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDelete
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agora', data_atual),
    path('', ProductListView.as_view() , name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create' ),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail' ),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update' ),
    path('product/delete/<int:pk>', ProductDelete.as_view(), name='product-delete' ),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
