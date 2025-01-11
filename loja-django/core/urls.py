
from django.contrib import admin
from django.urls import path
from app.views import data_atual
from app.views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agora', data_atual),
    path('', ProductListView.as_view() )
]
