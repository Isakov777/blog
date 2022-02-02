from django.shortcuts import redirect, render
from comments.models import Comment

def update_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        text = request.POST.get('text')
        comment.text = text
        comment.save()
        return redirect('index')
    return render(request, 'comments/update.html')

def delete_comment(request,id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('index')
    return render(request, 'comments/delete.html')



# def update(request,id):
#     post = Post.objects.get(id=id)
#     if request.method =='POST':
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             post.text = form.cleaned_data['text']
#             post.image = form.cleaned_data['image']
#             post.save()
#             return redirect('home')
#     else:
#         form=PostForm()
#     return render(request,'posts/update.html',{'form':form})
