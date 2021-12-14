from django.urls import path
from apps.posts.views import *

app_name = "posts"

urlpatterns = [
    path('post/crear', PostCreateView.as_view(), name='crearPost'),
    path('post/<int:pk>', PostShowView.as_view(), name='mostrarPost'),
    path('post/editar/<int:pk>', PostEditView.as_view(), name='editarPost'),
    path('post/eliminar/<str:pk>', PostDeleteView.as_view(), name='deletePost'),
    path('post/like/<str:pk>', like_view, name='likesPost'),
    path('post/dislike/<str:pk>', dislike_view, name='dislikesPost'),
    path('post/listar', PostListView.as_view(), name='listarPost'),
]