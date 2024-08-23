from django.urls import path, include
from .views import UserSignupView, LoginView, CategoriesView, SubCategoryView, UserScapeView

app_name = "user"
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="user-signup"),
    path('login/', LoginView.as_view(), name="user-login"),
    path('category', CategoriesView.as_view(), name="user-category"),
    path('sub-category/<int:id>', SubCategoryView.as_view(), name="user-category"),

    path('user-scape/', UserScapeView.as_view(), name="user-userscape")

]
