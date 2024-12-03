from django.contrib import admin
from .models import Posts, Comment, Profile, ProfileReport
# Register your models here.

admin.site.register(Posts)
admin.site.register(Comment)
admin.site.register(Profile)

@admin.register(ProfileReport)
class ProfileReportAdmin(admin.ModelAdmin):
    list_display = ('reported_by', 'reported_user', 'reason', 'report_date')
    list_filter = ('report_date',)
    search_fields = ('reported_by__username', 'reported_user__username', 'reason')