from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', ForumHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ForumCategory.as_view(), name='category'),
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('create_profile_page', CreateProfilePageView.as_view(), name='create_user_profile'),
    path('post/<int:pk>/update', NewsUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', NewsDeleteView.as_view(), name='delete_post'),
]