from django.urls import path
from .views import HomeView, Detail, AddPostView, UpdatePost, DeletePost, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', Detail.as_view(), name="detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>',UpdatePost.as_view(), name="update_post"),
    path('article/<int:pk>/remove',DeletePost.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]


