from django.contrib import admin
from workout.models import Exercise, Level,Category
# Register your models here.
admin.site.register(Level)
admin.site.register(Category)
admin.site.register(Exercise)