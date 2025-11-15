from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from coches.views import CocheViewSet


router = routers.DefaultRouter()
router.register('coches', CocheViewSet)

urlpatterns = [
    path('' includes(views.home))
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
