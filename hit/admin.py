from django.contrib import admin
from .models import HitCount  # Import your model


@admin.register(HitCount)
class HitCountAdmin(admin.ModelAdmin):
    # Include 'id' in the list_display
    list_display = ['id', 'endpoint', 'hits']
