from django.contrib import admin
from .models import Header, Education, About, Experience, Skill, Project, SocialNetwork

class ProjectAdmin(admin.ModelAdmin):
    list_display=("title","description","created_at")
    search_fields=("title",)
class HeaderAdmin(admin.ModelAdmin):
    list_display=("title","description","created_at","position","email","available")
    search_fields=("title",)
    
class EducationAdmin(admin.ModelAdmin):
    list_display=("specialization","institution","created_at","subjects","start_date","end_date")
    search_fields=("specialization","institution")
class ExperienceAdmin(admin.ModelAdmin):
    list_display=("company","created_at","position","start_date","end_date")
    search_fields=("company","position")
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display=("title","link","created_at","priority")
    search_fields=("title","link")
# Register your models here.
admin.site.register(Header, HeaderAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(About)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill)
admin.site.register(Project, ProjectAdmin)
admin.site.register(SocialNetwork,SocialNetworkAdmin)