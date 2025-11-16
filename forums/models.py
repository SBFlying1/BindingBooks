from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class forums(models.Model):
    forum_id = models.AutoField(primary_key=True)
    forum_name = models.TextField(null=False)
    forum_description = models.TextField()
    owner = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL
    )  # this is so if the owner is deleted, the owner here is simply set to null
    forum_tags = models.JSONField(default=list)
    start_date = models.DateField(null=True, blank=True)
    meeting_day = models.CharField(
        max_length=10,
        choices=[
            ("Mon", "Monday"),
            ("Tue", "Tuesday"),
            ("Wed", "Wednesday"),
            ("Thu", "Thursday"),
            ("Fri", "Friday"),
            ("Sat", "Saturday"),
            ("Sun", "Sunday"),
        ],
        null=True,
        blank=True,
    )
    meeting_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        owner_name = (
            self.owner.name if self.owner else "Unknown owner"
        )  # changed so having null owner doesn't give errors -sam
        return f"{self.forum_name} (owned by {owner_name})"


class forum_post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    forum = models.ForeignKey(forums, on_delete=models.CASCADE, related_name="posts")
    post_text = models.TextField(null=True, blank=True)
    post_reactions = models.JSONField(default=list)

    def __str__(self):
        author_name = (
            self.author.name if self.author else "Unknown author"
        )  # changed so having null owner doesnt give errors -sam
        return f"{author_name} said: {self.post_text}"


class forum_comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(
        forum_post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    comment_text = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        author_name = (
            self.author.name if self.author else "Unknown author"
        )  # null owner doesnt give errors -sam
        return f"Comment by {author_name}"
