from django.urls import path

from core.views import HomeTypeView, TypeView, HomeView, RequestView

urlpatterns = [
    path('home-type/', HomeTypeView.as_view()),
    path('type/', TypeView.as_view()),
    path('home/', HomeView.as_view()),
    path('request/', RequestView.as_view()),
]