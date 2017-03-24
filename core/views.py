from django.shortcuts import render
from django.http import HttpResponse

def test(request, post_id=None, blog_id=None):
    #return HttpResponse('Test passed, post_id = {}, blog_id = {}'. format(post_id, blog_id))
    return render(request, "core/file.html", {"post_id" : post_id, "blog_id" : blog_id})