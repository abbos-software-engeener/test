from django.contrib import admin
from .models import HomeType, Type, Home, Request

admin.site.register(HomeType)
admin.site.register(Type)


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('home_type', 'first_payment', 'amount')
    list_display_links = list_display

    def has_add_permission(self, request):
        return False


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'home', 'is_seen', 'created_at')
    list_display_links = list_display

    def has_add_permission(self, request):
        return False


