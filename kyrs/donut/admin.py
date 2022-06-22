from django.contrib import admin
from .models import CustomUsers, Posts, LikesPost, Facts

admin.site.register(CustomUsers)
admin.site.register(Posts)
admin.site.register(LikesPost)
admin.site.register(Facts)


