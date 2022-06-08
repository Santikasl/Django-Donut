from django.contrib import admin
from .models import CustomUsers
from .models import Posts
from .models import LikesPost


admin.site.register(CustomUsers)
admin.site.register(Posts)
admin.site.register(LikesPost)

