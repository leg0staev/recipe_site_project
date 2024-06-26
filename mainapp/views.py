from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from mainapp.models import Recipe
from random import randint


class MainRecipeListView(ListView):
    model = Recipe
    template_name = 'mainapp/index.html'
    queryset = Recipe.objects.order_by('?')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['recipes'] = context.pop('object_list')
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'mainapp/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context
