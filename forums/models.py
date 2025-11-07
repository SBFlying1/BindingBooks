from django.db import models
from accounts.models import base_user

class forums(models.Model):
    forum_id = models.AutoField(primary_key=True)
    forum_name = models.TextField(null=False)
    forum_description = models.TextField()
    owner = models.ForeignKey(base_user,null=True,on_delete=models.SET_NULL) #this is so if the owner is deleted, the owner here is simply set to null
    forum_tags = models.JSONField(default=list)
    
    def __str__(self):
        return f"{self.forun_name} which is owned by {self.owner.name}"


class forum_post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(base_user,null=True,on_delete=models.SET_NULL)
    post_text = models.TextField
    post_reactions = models.JSONField(default=list)

    def __str__(self):
        return f"{self.author.name} said this: {self.post_text}"