from django.shortcuts import render, get_object_or_404, redirect
from .models import forums, forum_post, forum_comment


# remove once base user returning correctly
def get_forum_user(request):
    if not request.user.is_authenticated:
        return None

    try:
        # If base_user exists for this Django user
        return request.user.base_user
    except:
        return None


def forum_list(request):
    all_forums = forums.objects.all()
    return render(request, "forums/forum_list.html", {"forums": all_forums})


def forum_detail(request, forum_id):
    forum = get_object_or_404(forums, pk=forum_id)
    posts = forum.posts.all()  # shows only this forums posts
    return render(request, "forums/forum_detail.html", {"forum": forum, "posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(forum_post, pk=post_id)
    comments = post.comments.all()

    return render(
        request, "forums/post_detail.html", {"post": post, "comments": comments}
    )


def create_post(request, forum_id):
    forum = get_object_or_404(forums, pk=forum_id)

    if request.method == "POST":
        text = request.POST.get("text")
        author = get_forum_user(request)  # change once base user working correctly

        forum_post.objects.create(forum=forum, author=author, post_text=text)

        return redirect("forum_detail", forum_id=forum_id)

    return render(request, "forums/create_post.html", {"forum": forum})


def create_forum(request):
    if request.method == "POST":
        # get fields from post
        name = request.POST.get("forum_name")
        description = request.POST.get("forum_description")
        tags = request.POST.get("forum_tags")
        start_date = request.POST.get("start_date")
        meeting_day = request.POST.get("meeting_day")
        meeting_time = request.POST.get("meeting_time")

        owner = get_forum_user(
            request
        )  # change once base user working correctly/i figure out what im doin wrong

        # Convert comma-separated tags into a list
        try:
            tag_list = [t.strip() for t in tags.split(",")] if tags else []
        except:
            tag_list = []

        # Save the new forum
        forums.objects.create(
            forum_name=name,
            forum_description=description,
            forum_tags=tag_list,
            owner=owner,  # owner can be none for now!!! dont forget to change
            start_date=start_date or None,
            meeting_day=meeting_day or None,
            meeting_time=meeting_time or None,
        )

        return redirect("forum_list")  # back to list page

    # show empty form
    return render(request, "forums/create_forum.html")


# comments on individual posts in a given forum
def create_comment(request, post_id):
    post = get_object_or_404(forum_post, pk=post_id)

    if request.method == "POST":
        text = request.POST.get("text")

        # owner can be none for now, dont forget to change
        author = get_forum_user(request)

        forum_comment.objects.create(post=post, author=author, comment_text=text)

        return redirect("post_detail", post_id=post_id)  # return to forum page

    return redirect("post_detail", post_id=post_id)
