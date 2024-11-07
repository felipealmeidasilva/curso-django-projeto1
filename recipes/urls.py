from django.urls import path

from recipes.views import sobre, contato


urlpatterns = [
    path('sobre/', sobre),
    path('contato/', contato),
]
