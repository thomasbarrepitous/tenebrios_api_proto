"""
URL configuration for tenebrios_api project.

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
from django.urls import path, include
from api_dashboard import views as weather_views
from api_tracability import views as tracability_views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'/co2-captures', weather_views.C02ViewSet)
router.register(r'/humidity-captures', weather_views.HumidityViewSet)
router.register(r'/temperature-captures', weather_views.TemperatureViewSet)
router.register(r'/actions', tracability_views.ActionDetailViewSet)


urlpatterns = [
    path('api', include(router.urls)),
    path('api-auth', include('rest_framework.urls')),
]
