from django.urls import path, include
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListView.as_view(), name='blogpost-list'),
    path('blogposts/create/', views.BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroyView.as_view(), name='blogpost-retrieve-update-destroy'),
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comments/create/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyView.as_view(), name='comment-retrieve-update-destroy'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/create/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
    path('tags/', views.TagListView.as_view(), name='tag-list'),
    path('tags/create/', views.TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', views.TagRetrieveUpdateDestroyView.as_view(), name='tag-retrieve-update-destroy'),
]
