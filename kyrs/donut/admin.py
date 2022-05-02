from django.contrib import admin
from .models import CustomUsers
from .models import Posts


admin.site.register(CustomUsers)
admin.site.register(Posts)

