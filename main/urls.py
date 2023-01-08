from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('<int:id>', views.product_details, name='product_details'),
   path('create/', views.create_product, name='create_product' )
]


urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)