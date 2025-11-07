from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class base_user(get_user_model()):

    user_id = models.AutoField(primary_key=True)
    #password, email, and names are already implemenet with the base django user model that we are inheriting from
    user_bio = models.TextField()
    user_owned_books = models.JSONField() 



    def __str__(self):
        return f"{self.first_name} {self.last_name}"