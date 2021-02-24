from django.contrib import admin
from .models import Category, Post

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    # mostrará los campos como solo lectura
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    # mostrará los campos como solo lectura
    readonly_fields = ('created', 'updated')
    # mostrará las columnas que deseo
    list_display = ('title', 'author', 'published',
                    'created', 'post_categories')
    # organiza la información según una tupla, por eso debo dejarlo con la coma vacío
    ordering = ('author',)
    # generar la barra de buscador. Como Author es una foreingkey, debo ponerlo así author__username para indicarle lo que quiero ver
    search_fields = ('title', 'content', 'created', 'author__username')
    date_herarchy = 'published'  # jerarquizar entradas por fechas
    list_filter = ('author__username',)

    # le paso 'self' porque así hago referencia a la clase, 'obj' hace referencia a cada elemento ''fila''
    def post_categories(self, obj):
        # hago un recorrido de cada elemento y saco su categoría
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"  # puse el nombre de la columna


# Aquí importé el modelo que creé antes.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
