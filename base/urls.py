from django.urls import path
from .views  import GetInfoView
urlpatterns = [
   
    path('data/<int:id>',GetInfoView.as_view()),
]