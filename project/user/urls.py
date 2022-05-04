from django.urls import include, path
# from user import views
from . import views
app_name= "user"

# from user import views


urlpatterns=[
    
    path('signup/', views.CreateSignUP.as_view()),
    path('getall/', views.GetAllData.as_view()),
    path('login/', views.DoLogin.as_view()),
    path('deldata/<int:pk>/', views.DeleteData.as_view()),
    ]






