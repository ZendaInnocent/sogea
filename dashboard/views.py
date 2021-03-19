from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Sum
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

from posts.models import Post, PostBookmark
from accounts.models import Profile
from .forms import ProfileForm


@login_required
def dashboard(request):

    user = request.user

    posts = Post.objects.filter(author=user).order_by('-created_at')

    post_views = posts.aggregate(total=Sum('view_count'))

    profile = Profile.objects.get(user=user)
    following = profile.following.count()

    context = {
        'posts':posts,
        'post_views':post_views,
        'total_post':posts.count(),
        'following':following,
    }

    template_name = 'dashboard/index.html'

    return render(request, template_name, context)

@login_required
def profile_update(request, id):

    profile = get_object_or_404(Profile, user_id=id)

    if profile.user != request.user: 
        raise PermissionDenied()

    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if form.is_valid():
        form.save()

        return redirect(reverse("dashboard:profile_update", kwargs={
            'id': id
        }))
        messages.success(request, "You are successfully update profile")
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form':form
    }

    template_name = 'dashboard/profile_update.html'

    return render(request, template_name, context)


def reading_list(request):

    posts = PostBookmark.objects.all().order_by('-created_at')

    context = {'posts':posts}
    
    template_name = 'dashboard/reading_list.html'

    return render(request, template_name, context)
