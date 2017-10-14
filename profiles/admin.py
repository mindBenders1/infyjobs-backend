from django.contrib import admin
from .models import UserProfile, AddExperience, AddProject, AddMembers

admin.site.register(UserProfile)
admin.site.register(AddExperience)
admin.site.register(AddProject)
admin.site.register(AddMembers)

