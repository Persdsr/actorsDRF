from django.contrib import admin

from .models import Actor, Category


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
