from django.contrib import admin
from .models import CafeInfo, Category, MenuItem, GalleryImage, Reservation, ContactMessage


@admin.register(CafeInfo)
class CafeInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not CafeInfo.objects.exists()  # only one allowed


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'vegetarian', 'featured', 'available')
    list_filter = ('category', 'available', 'featured', 'vegetarian')
    list_editable = ('price', 'featured', 'available')
    search_fields = ('name', 'description')


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time', 'guests', 'status')
    list_filter = ('status', 'date')
    list_editable = ('status',)
    search_fields = ('name', 'phone', 'email')
    date_hierarchy = 'date'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created', 'is_read')
    list_filter = ('is_read',)
    list_editable = ('is_read',)
    readonly_fields = ('created',)