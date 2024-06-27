from django.urls import path
from .views import MainRecipeListView, RecipeDetailView, RegisterView, RegistrationSuccessView, LogoutSuccessView, AllRecipesView
from django.contrib.auth import views as auth_views

app_name = 'mainapp'

urlpatterns = [
    path('', MainRecipeListView.as_view(), name='index'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    # path('register/', register, name='register'),
    path('register/', RegisterView.as_view(), name='register'),
    path('registration_success/', RegistrationSuccessView.as_view(), name='registration_success'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout_success/', LogoutSuccessView.as_view(), name='logout_success'),
    path('logout/', auth_views.LogoutView.as_view(next_page='mainapp:logout_success'), name='logout'),
    path('all_recipes/', AllRecipesView.as_view(), name='all_recipes'),

]
