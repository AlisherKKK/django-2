from django.contrib import admin

from .models import Person, Experience, Education, Skills

admin.site.register(Person)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skills)
