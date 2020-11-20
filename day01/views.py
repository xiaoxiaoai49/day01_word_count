from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'home2.html')

def tongji(request):
    total_count=len(request.GET['text'])
    user_text=request.GET['text']

    word_dict={}

    for word in user_text:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]+=1

    soted_dict=sorted(word_dict.items(),key=lambda w:w[1],reverse=True)

    return render(request,'count.html',
                  {'count':total_count,'text':user_text,
                   'wordict':word_dict,'sortedict':soted_dict})