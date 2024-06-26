from django.urls import path
from .views import MainRecipeListView, RecipeDetailView

app_name = 'mainapp'

urlpatterns = [
    path('', MainRecipeListView.as_view(), name='home'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
]
