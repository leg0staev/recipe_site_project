from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe
from .forms import UserRegistrationForm, RecipeForm


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


class RegisterView(FormView):
    template_name = 'mainapp/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('mainapp:registration_success')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        login(self.request, new_user)
        return super().form_valid(form)


class RegistrationSuccessView(TemplateView):
    template_name = 'mainapp/registration_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вы успешно зарегистрировались'
        return context


class LogoutSuccessView(TemplateView):
    template_name = 'mainapp/logout_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вы успешно вышли'
        return context


class AllRecipesView(ListView):
    model = Recipe
    template_name = 'mainapp/all_recipes.html'
    queryset = Recipe.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все рецепты'
        context['recipes'] = context.pop('object_list')
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'mainapp/recipe_form.html'
    success_url = reverse_lazy('mainapp:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить рецепт'
        return context


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'mainapp/recipe_form.html'
    success_url = reverse_lazy('mainapp:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать рецепт'
        return context
