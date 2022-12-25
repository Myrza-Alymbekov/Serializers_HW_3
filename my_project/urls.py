from django.contrib import admin
from django.urls import path, include
from products import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('item', views.ItemViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/brand/', views.BrandCreateListView.as_view()),
    path('api/brand/<int:pk>/', views.BrandRetrieveUpdateDestroyAPIView.as_view()),
    path('api/category/', views.create_category),
]
