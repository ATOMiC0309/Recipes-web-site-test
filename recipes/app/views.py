from django.shortcuts import render, redirect
from .models import Category, Recipe
from .forms import RecipeForm, CategoryForm
# Create your views here.


def index(request):
    """Home page"""

    categories = Category.objects.all()
    recipes = Recipe.objects.all()
    context = {
        "categories": categories,
        "recipes": recipes
    }

    return render(request, 'app/index.html', context=context)


def all_recipes_by_category(request, category):
    """for View recipes by category"""

    categories = Category.objects.all()
    category = Category.objects.get(name=category)
    recipes = Recipe.objects.filter(category=category)

    context = {
        "categories": categories,
        "recipes": recipes
    }

    return render(request, 'app/index.html', context=context)


def recipe_detail(request, pk):
    """for Recipe view detail"""

    recipe = Recipe.objects.get(pk=pk)

    context = {
        "recipe": recipe,
    }

    return render(request, 'app/recipe_detail.html', context=context)


def recipe_create(request):
    """for Recipe create """

    recipe_form = RecipeForm(data=request.POST, files=request.FILES)
    if recipe_form.is_valid():
        recipe_form.save()
        return redirect('index')

    recipe_form = RecipeForm()
    context = {
        'recipe_form': recipe_form,
    }
    return render(request, 'app/recipe_form.html', context=context)


def recipe_update(request, pk):
    """for  Recipe update(change)"""

    recipe = Recipe.objects.get(pk=pk)

    recipe_form = RecipeForm(data=request.POST or None, instance=recipe, files=request.FILES or None)
    if recipe_form.is_valid():
        recipe_form.save()
        return redirect('index')

    context = {
        'recipe_form': recipe_form,
    }
    return render(request, 'app/recipe_form.html', context=context)


def recipe_delete(request, pk):
    """for recipe delete"""

    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('index')

    return render(request, 'app/recipe_delete.html', {"recipe": recipe})


def all_categories(request):
    """get all category"""

    categories = Category.objects.all()
    return render(request, 'app/categories.html', context={"categories": categories})


def category_create(request):
    """for category create"""

    category_form = CategoryForm(data=request.POST)
    if category_form.is_valid():
        category_form.save()
        return redirect('all_categories')

    category_form = CategoryForm()
    context = {
        'category_form': category_form,
    }
    return render(request, 'app/category_form.html', context=context)


def category_update(request, pk):
    """for category update"""

    category = Category.objects.get(pk=pk)

    category_form = CategoryForm(data=request.POST or None, instance=category)
    if category_form.is_valid():
        category_form.save()
        return redirect('all_categories')

    context = {
        'category_form': category_form,
    }
    return render(request, 'app/category_form.html', context=context)


def category_delete(request, pk):
    """for category update"""

    category = Category.objects.get(pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('all_categories')

    return render(request, 'app/category_delete.html', {"category": category})



