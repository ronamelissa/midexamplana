from django.urls import path
from . import views

app_name="votes"
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('createposition/', views.createposition, name='createposition'),
    path('<int:candidate_id>/', views.detail, name='detail'),
    path('<int:candidate_id>/update', views.update, name ='update'),
]
