"""
URL configuration for shop_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from shop_api import settings
from product.views import products_categories_api_view, product_review_api_view, products_api_view, \
    categories_retrieve_api_view, review_retrieve_api_view, products_retrieve_api_view

urlpatterns = [
    path('api/''admin/', admin.site.urls),
    path('api/v1/categories/<int:id>/', products_categories_api_view),
    path('api/v1/categories/', categories_retrieve_api_view),
    path('api/v1/reviews/', product_review_api_view),
    path('api/v1/reviews/<int:id>/', review_retrieve_api_view),
    path('api/v1/products/', products_api_view),
    path('api/v1/products/<int:id>/', products_retrieve_api_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
