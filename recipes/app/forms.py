from django import forms
from .models import Recipe, Category


class RecipeForm(forms.ModelForm):
    """this class is a form for creating and updating a recipe"""
    class Meta:
        model = Recipe
        fields = ["name", "content", "category", "published", "photo"]


class CategoryForm(forms.ModelForm):
    """this class is a form for creating and updating a category"""

    class Meta:
        model = Category
        fields = ["name", "published"]
