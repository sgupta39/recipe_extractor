from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from register.models import *
# Create your views here.

class WriteRecipeApiView(APIView):
    # 1. List all
    print('hey')
    def get(self, request, *args, **kwargs):
        print('123')
        return render(request, 'write_recipe/write_recipe.html')

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request)
        print(request.data["title"])
        print(request.data["feedurl[]"])
        print(request.data["recipe"])
        print()


        print(request.user)
        print(request.user.first_name)
        recipe = ExtractedRecipe.objects.create(
                    userId = request.user,
                    recipe_template = request.data["recipe"],
                    recipe_title = request.data["title"]
                )

        print(recipe)

        Ingredients.objects.create(
                    recipeId = recipe,
                    ingredient_name = request.data["feedurl[]"]
                )
 
       

        return render(request, 'write_recipe/write_recipe.html')

class UploadLinkApiView(APIView):
    # 1. List all
    print('In Upload Link')
    def get(self, request, *args, **kwargs):
        print('123')
        #return render(request, 'write_recipe/write_recipe.html')
        return render(request, 'upload_link/upload_link.html')
    
def user_homepage(request):

    # 1. List all
    print('homepage')
    queryset = ExtractedRecipe.objects.filter(userId=request.user)
    
    return render(request, "userhomepage/userhomepage.html", {'queryset': queryset})

'''def get_Recipe(request):

        print('*********  get_recipe func ***************')

        recipeId=request.GET.get('recipe_id')
        recipe = ExtractedRecipe.objects.get(id=recipeId)
        ingredient=Ingredients.objects.filter(recipeId=recipeId)
        
        return render(request,'write_recipe/recipe.html',{'recipe': recipe, 'ingredients': ingredient})
'''


class GetRecipeView(APIView):

    def get(self, request, *args, **kwargs):

        print('*********  get_recipe func ***************')

        recipeId=request.GET.get('recipe_id')
        print('get recipe id',recipeId)
        recipe = ExtractedRecipe.objects.get(id=recipeId)
        ingredient=Ingredients.objects.filter(recipeId=recipeId)
        
        return render(request,'write_recipe/recipe.html',{'recipe': recipe, 'ingredients': ingredient})

    def post(self, request, *args, **kwargs):

        print('post write recipe')

        recipeId=request.GET.get('recipe_id')

        recipe = ExtractedRecipe.objects.get(id=recipeId)
        ingredient= Ingredients.objects.get(recipeId=recipeId)

        recipe.recipe_title=request.data['title']
        recipe.recipe_template=request.data['recipe']
        ingredient.ingredient_name = request.data['feedurl[]']

        recipe.save()
        ingredient.save()

        queryset = ExtractedRecipe.objects.filter(userId=request.user)
        print(recipe.recipe_title)
        print(recipe.recipe_template)
        print(ingredient.ingredient_name)

        return render(request, 'userhomepage/userhomepage.html', {'queryset': queryset})
