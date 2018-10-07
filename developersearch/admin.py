from django.contrib import admin

# Register your models here.
from .models import Developers, Interviews, Languages, ProgrammingLanguages


class DeveloperAdmin(admin.ModelAdmin):
    list_display = (['email'])
    search_fields = (['email'])



class DeveloperInterviewAdmin(admin.ModelAdmin):
    list_display = (['developer', 'score', 'comment'])
    search_fields = (['developer__email'])

admin.site.register(Developers, DeveloperAdmin)
admin.site.register(Interviews, DeveloperInterviewAdmin)
admin.site.register(Languages)
admin.site.register(ProgrammingLanguages)
