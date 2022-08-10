from django.contrib import admin
from .models import News, PC, Accessory, Type


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'photo', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'created_at')
    fields = ('title', 'slug', 'content', 'photo')
    prepopulated_fields = {"slug": ("title",)}

class PCAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cpu', 'gpu', 'ram', 'memory', 'photo', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'cpu', 'gpu', 'ram', 'memory', 'price')
    fields = ('title', 'slug', 'content', 'photo', 'cpu', 'gpu', 'ram', 'memory', 'price')
    prepopulated_fields = {"slug": ("title",)}

class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'types', 'photo', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'types', 'price')
    fields = ('title', 'slug', 'content', 'types', 'photo', 'price')
    prepopulated_fields = {"slug": ("title",)}

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', )
    fields = ('title', )
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(News, NewsAdmin)
admin.site.register(PC, PCAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Accessory,  AccessoryAdmin)
