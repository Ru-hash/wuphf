from django.urls import path
from .views import (PostCreateView,
					PostDetailView,
					start_view,
					PostListView,
					PostUpdateView,
					PostDeleteView,
					UserPostListView)
app_name='my_blog'
urlpatterns=[
	
	path('',PostListView.as_view(),name='home') ,
	path('add',PostCreateView.as_view(),name='add') ,
	path('update/<int:pk>',PostUpdateView.as_view(),name='update') ,
	path('user/<str:username>',UserPostListView.as_view(),name='user_post') ,
	path('delete/<int:pk>',PostDeleteView.as_view(),name='delete') ,
	path('detail/<int:pk>',PostDetailView.as_view(),name='detail') ,
] 