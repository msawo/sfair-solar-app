from django.contrib import admin

from collection.models import Profile

# set up automated slug creation
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'address',)
    prepopulated_fields = {'slug': ('name',)}




admin.site.register(Profile, ProfileAdmin) # Register the model
