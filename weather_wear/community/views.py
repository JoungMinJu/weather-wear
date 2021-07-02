from django.shortcuts import render, redirect, get_object_or_404
from .models import Community, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def show(request):
    communities = Community.objects.order_by('-pub_date')
    return render(request, 'community/show.html', {'communities':communities})

def detail(request, id):
    community = get_object_or_404(Community, id = id) 
    all_comments = community.comments.order_by('-created_at')
    community.view_count += 1
    community.save()
    return render(request, 'community/detail.html', {'community':community, 'comments':all_comments})

def new(request):
    return render(request, 'community/new.html')    

def create(request):
    new_community = Community()
    new_community.title = request.POST['title']
    new_community.writer = request.user
    new_community.pub_date = timezone.now()
    new_community.body = request.POST['body']
    new_community.image = request.FILES.get('image')
    new_community.weather = request.POST['weather']
    new_community.gender = request.POST['gender']
    new_community.save()
    return redirect('community:detail', new_community.id)

def edit(request, id):
    edit_community = Community.objects.get(id = id)
    return render(request, 'community/edit.html', {'community': edit_community})

def update(request, id):
    update_community = Community.objects.get(id = id)
    update_community.title = request.POST['title']
    update_community.writer = request.user
    update_community.pub_date = timezone.now()
    update_community.body = request.POST['body']
    update_community.image = request.FILES.get('image')
    update_community.weather = request.POST['weather']
    update_community.gender = request.POST['gender']
    update_community.save()
    return redirect('community:detail', update_community.id)

def delete(request, id):
    delete_community = Community.objects.get(id = id)
    delete_community.delete()
    return redirect('community:show')

def create_comment(request, community_id):
    if request.method == "POST":
        community = get_object_or_404(Community, pk=community_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, community=community)
    return redirect('community:detail', community_id)

def update_comment(request, comment_id):
    comment=get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        community_id = comment.community.id
        comment.content=request.POST.get('content')
        comment.save()
        return redirect('community:detail', community_id)
    return render(request, 'community/update_comment.html',{"comment":comment})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    community_id = comment.community.id
    comment.delete()
    return redirect('community:detail', community_id)
