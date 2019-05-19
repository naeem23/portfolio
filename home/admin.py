from django.contrib import admin
from .models import TitleSubtitle, Home, About, Skill, Service, Project, Feedback, FollowMe, Contact

class HomeAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'up_heading', 'down_heading')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('s_title', 's_icon')
    search_fields = ['s_title']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','category', 'clients')
    search_fields = ['project_name', 'category', 'clients', 'tools']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'profession')

class ContactAdmin(admin.ModelAdmin):
    search_fields = ['email', 'subject', 'name', 'message']

admin.site.register(TitleSubtitle)
admin.site.register(Home,HomeAdmin)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(FollowMe)
admin.site.register(Contact, ContactAdmin)
