from django.contrib import admin
from .models import forums, forum_post, forum_comment

admin.site.register(forums)
admin.site.register(forum_post)
admin.site.register(forum_comment)
