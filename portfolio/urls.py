from . import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('potfolios/<int:pk>',views.portfolio_detail,name='portfolio'),
    
]
