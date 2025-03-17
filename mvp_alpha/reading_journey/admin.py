from django.contrib import admin
from .models import Journey, Archipelago, Island, LessonCompletion

class IslandInline(admin.TabularInline):
    model = Island
    extra = 0 # Number of empty forms to display

class ArchipelagoAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [IslandInline]
    
admin.site.register(Journey)
admin.site.register(Archipelago, ArchipelagoAdmin)
admin.site.register(Island)
admin.site.register(LessonCompletion)