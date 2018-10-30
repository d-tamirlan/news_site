from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('news', views.NewsViewSet)


urlpatterns = [
    path('categories-list/', views.CategoriesList.as_view(), name='categories-list'),
    path('', include(router.urls))
]