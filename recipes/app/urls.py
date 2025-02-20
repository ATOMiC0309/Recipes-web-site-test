from django.urls import path
from .views import (index, all_recipes_by_category, recipe_detail, recipe_create, recipe_update, recipe_delete,
                    all_categories, category_create, category_update, category_delete)
urlpatterns = [
    path('', index, name="index"),
    path('category/<str:category>/', all_recipes_by_category, name="recipes_by_category"),
    path('recipe-detail/<int:pk>/', recipe_detail, name="recipe_detail"),
    path('recipe-create/', recipe_create, name="recipe_create"),
    path('recipe-update/<int:pk>/', recipe_update, name="recipe_update"),
    path('recipe-delete/<int:pk>/', recipe_delete, name="recipe_delete"),
    path('all-category/', all_categories, name="all_categories"),
    path('category-create/', category_create, name="category_create"),
    path('category-update/<int:pk>/', category_update, name="category_update"),
    path('category-delete/<int:pk>/', category_delete, name="category_delete"),
]
