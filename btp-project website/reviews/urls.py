
from django.urls import path,include
from . import views
urlpatterns = [

    path('search',views.search,name='search'),
    path('allreviews',views.allreviews,name='allreviews'),
    path('create',views.create,name='create'),
    path('<int:review_id>', views.detail, name='detail'),
    path('<int:review_id>/upvote', views.upvote, name='upvote'),
]
