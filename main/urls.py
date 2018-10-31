from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('news', views.NewsViewSet)


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('categories-list/', views.CategoriesList.as_view(), name='categories-list'),
    path('', include(router.urls))
]
