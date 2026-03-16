from django.contrib import messages

import django
from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.models import User


def recipes(request):

    if request.method == 'POST':

        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_ingredients = data.get('recipe_ingredients')

        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_ingredients=recipe_ingredients,
            recipe_image=recipe_image
        )

        return redirect('/recipes/')


    queryset = Recipe.objects.all()

    search_query = request.GET.get('search')

    if search_query:
        queryset = queryset.filter(recipe_name__icontains=search_query)


    # ingredients split for template
    for recipe in queryset:

        if recipe.recipe_ingredients:
            recipe.ingredients_list = [
                i.strip() for i in recipe.recipe_ingredients.split(',')
            ]
        else:
            recipe.ingredients_list = []


    context = {
        'recipes': queryset,
        'search_query': search_query
    }

    return render(request, 'recipes.html', context)


def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == 'POST':

        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()

        return redirect('/recipes/')


    
    context = {'recipe': queryset}

    return render(request, 'update_recipe.html', context)



def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
 

    return redirect('/recipes/')


def recipe_detail(request, id):

    recipe = Recipe.objects.get(id=id)

    ingredients = []

    if recipe.recipe_ingredients:
        ingredients = [i.strip() for i in recipe.recipe_ingredients.split(',')]

    context = {
        "recipe": recipe,
        "ingredients": ingredients
    }

    return render(request, "recipe_detail.html", context)









def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')


    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:




    return render(request, 'login.html')    












def register_page(request):
    """if request.user.is_authenticated:
        return redirect('/')"""

    if request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')git
        
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken. Please choose another.')
            return redirect('/register/')

        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        user.set_password(password)
        user.save() 

        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('/login/')

    return render(request, 'register.html')