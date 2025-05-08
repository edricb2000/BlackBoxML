# Register your models here.

from django.contrib import admin
from .models import TrainedModel, UserCredits, PredictionLog

class TrainedModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'uploaded_at', 'file_link')
    list_filter = ('version', 'uploaded_at')
    search_fields = ('name', 'version')
    readonly_fields = ('uploaded_at',)
    
    def file_link(self, obj):
        if obj.file:
            return f'<a href="{obj.file.url}">Download</a>'
        return "No file"
    file_link.allow_tags = True
    file_link.short_description = 'Model File'

class UserCreditsAdmin(admin.ModelAdmin):
    list_display = ('user', 'credits')
    list_editable = ('credits',)  # Edit credits directly from list view
    search_fields = ('user__username',)

class PredictionLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'model', 'timestamp', 'credits_used')
    list_filter = ('model', 'timestamp')
    readonly_fields = ('timestamp',)  # Prevent editing of timestamps
    date_hierarchy = 'timestamp'

# Register all models with their custom admin classes
admin.site.register(TrainedModel, TrainedModelAdmin)
admin.site.register(UserCredits, UserCreditsAdmin)
admin.site.register(PredictionLog, PredictionLogAdmin)


