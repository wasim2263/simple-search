from django.contrib import admin

# Register your models here.
from .models import Developers, Interviews, Languages, ProgrammingLanguages

admin.site.register(Developers)
admin.site.register(Interviews)
admin.site.register(Languages)
admin.site.register(ProgrammingLanguages)
