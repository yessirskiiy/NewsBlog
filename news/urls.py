from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import NewsList, NewsDetail, NewsCreate, NewsDelete, NewsEdit, UserLogin, UserRegistration, CommentCreate, \
    CommentDelete


urlpatterns =[
    path('', NewsList.as_view(), name='news'),
    path('post/<int:pk>/', NewsDetail.as_view(), name='post'),
    path('post_create/', NewsCreate.as_view(), name='post_create'),
    path('post_delete/<int:pk>/', NewsDelete.as_view(), name='post_delete'),
    path('post_edit/<int:pk>/', NewsEdit.as_view(), name='post_edit'),

    path('post/<int:post_id>/create_comment/', CommentCreate.as_view(), name='create_comment'),
    path('delete_comment/<int:pk>/', CommentDelete.as_view(), name='delete_comment'),

    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='news'), name='logout'),
    path('registration/', UserRegistration.as_view(), name='registration')

]

