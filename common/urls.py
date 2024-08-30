from django.urls import path
from .views import RegisterView, LoginView , delete_user_by_username , get_user_info , UsernameRetrievalView ,PasswordRetrievalView , update_user_info



app_name = 'common'

urlpatterns = [

    path('register/', RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path('delete/<str:username>/', delete_user_by_username, name='delete-user-by-username'),
    path('userinfo/<str:username>/', get_user_info, name='userinfo'),
    path('userinfo/update/<str:username>/', update_user_info, name='update-user-info'),
    path('findusername/', UsernameRetrievalView.as_view(), name='findusername'),
    path('findpassword/', PasswordRetrievalView.as_view(), name='findpassword'),



]

