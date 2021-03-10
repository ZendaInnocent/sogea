from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import HttpResponse

from posts.models import Post,PostBookmark
from accounts.models import Profile


def homepage(request):

    posts_list = Post.objects.all().order_by('-created_at')
   
    try:
        p_ft = Post.objects.get(featured=1)
        common_tags = Post.tags.most_common()[:4]
    except:
        pass

    if request.method =="POST":
        if request.POST.get("operation") == "like_submit" and request.is_ajax():
            content_id=request.POST.get("content_id",None)
            content=get_object_or_404(Post, pk=content_id)
            if content.likes.filter(id=request.user.id): #already liked the content
                content.likes.remove(request.user) #remove user from likes 
                liked=False
            else:
                content.likes.add(request.user) 
                liked=True

            context = {"likes_count":content.total_likes,"liked":liked,"content_id":content_id}

            return HttpResponse(json.dumps(context), content_type='application/json')

        already_liked=[]
        id=request.user.id
        for content in posts_list:
            if(content.likes.filter(id=id).exists()):
                already_liked.append(content.id)

        context = {"contents":contents,"already_liked":already_liked}
   
    template_name = 'main/index.html'

    context = {
        'posts_list':posts_list,
        'p_ft':p_ft,
        'common_tags':common_tags,
    }

    return render(request, template_name, context=context)



def post_detail(request, post_slug):

    try:
        post = get_object_or_404(Post, slug=post_slug)
        post.view_count += 1
        post.save()
    except ObjectDoesNotExist:
        raise Http404

    post_bookmarks = PostBookmark.objects.filter(post=post).count()

    if request.user.is_authenticated:
        post_state = PostBookmark.objects.filter(user=request.user, post=post)
        like_state = post.likes.filter(id=request.user.id)

        #follow
  
        view_profile = Profile.objects.get(pk=post.author.profile.pk)
 
        my_profile = Profile.objects.get(user=request.user)
  

        if view_profile.user in my_profile.following.all():
            follow = True
        elif view_profile == my_profile:
            follow = 'hide'
        else:
            follow = False

        print('follow:', follow)

        context = {'post':post,'post_state':post_state,'post_bookmarks':post_bookmarks,'like_state':like_state, 'follow':follow}

        template_name = 'main/post_detail.html'

        return render(request, template_name, context)

    context = {
        'post':post,
        'post_bookmarks':post_bookmarks,
    }

    template_name = 'main/post_detail.html'

    return render(request, template_name, context)