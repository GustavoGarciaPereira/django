from django.contrib import admin
from core.models import Pessoa

# Register your models here.
class BlogPostAdim(admin.ModelAdmin):
    list_display = ('title', 'time')



admin.site.register(Pessoa,BlogPostAdim)
