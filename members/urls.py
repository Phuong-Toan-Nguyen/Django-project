from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main page'),
    path('/', views.main),
    path('news/<int:id>', views.NewsDetail),
    path('story/<int:id>', views.StoryDetail),
    path('trailer/<int:id>', views.TrailerDetail),
    path('music/<int:id>', views.MusicDetail),
    path('blu-ray&DVD/<int:id>', views.BludvdDetail),
    path('Goods/<int:id>', views.GoodsDetail),
    
    path('testing/', views.testing, name='testing'),
    path('testing/news/<int:id>', views.GoodsDetail),
    
]




