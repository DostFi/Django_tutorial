from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
posts = [
    {
        "id":1,
        "title":'Let\'s explore python',
        "content":'Python Is Interpreted, High level, general purpose programming language. Widely used in the fields of web development, data science ane machine learning'
    },
    {
        "id":2,
        "title":'Let\'s explore Javascript',
        "content": 'Javascript Is Interpreted, High level, general purpose programming language, widely used in fieldsof web developments.'
    },
    {
        'id':3,
        'title':'Django the best web framework',
        "content": 'Django is used byalmost every big tech company like facebook, google, youtube, instagram etc'
    },

]
def home(request,):
    html = ""
    for post in posts:
        html += f'''
            <div>
            <a href="/post/{post['id']}/">
                <h1>{post['id']} - {post['title']}</h1></a>
                <p>{post['content']}</p>
            </div>
'''
    return HttpResponse(html)

def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        html = f'''
            <h1>{post_dict['title']}</h1>
            <p>{post_dict['content']}</p>
    '''
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("Post not available :-(")
    
def google(request,id):
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)