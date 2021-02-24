from django.contrib import admin
from .models import Link

# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    # mostrará los campos como solo lectura
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)
