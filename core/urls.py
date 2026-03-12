from django.contrib import admin
from django.urls import path
from vege.views import recipes, recipe_detail, delete_recipe, update_recipe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', recipes),

    path('recipes/', recipes),

    path('recipe/<int:id>/', recipe_detail, name='recipe_detail'),

    path('delete_recipe/<int:id>/', delete_recipe),

    path('update_recipe/<int:id>/', update_recipe),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)