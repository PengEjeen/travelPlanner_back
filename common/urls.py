from django.urls import path
from .views import RegisterView, LoginView , delete_user_by_username , get_user_info , UsernameRetrievalView ,PasswordRetrievalView



app_name = 'common'

urlpatterns = [

    path('register/', RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path('delete/', delete_user_by_username, name='delete'),
    path('userinfo/<str:username>/', get_user_info, name='userinfo'),
    path('findusername/', UsernameRetrievalView.as_view(), name='findusername'),
    path('findpassword/', PasswordRetrievalView.as_view(), name='findpassword'),



]

