from django.contrib import admin
from app import models

@admin.register(models.Create)
class AppAdmin(admin.ModelAdmin):
    list_display = 'id', 'user_name', 'password', #Mostrar como se fosse uma tabela
    ordering = '-id',
    #list_filter = ('created_date',)
    search_fields = 'id', 'user_name',
    list_per_page = 15
    list_max_show_all = 400
    list_editable = 'user_name',
    list_display_links = 'id',

