from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView

router = DefaultRouter()
router.register(r'', CategoryView)

urlpatterns = [
    path('', include(router.urls)),
]