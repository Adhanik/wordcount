from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')#we are returning a template now.A new page has to be loaded
def youth(request):
    return HttpResponse('<h1>Be the voice</h1>')#we are directly sending a HttpResponse.
def count(request):
    fulltext = request.GET['fulltext']#stores the sites url.
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    sortwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortwords})#displaying what the user entered in count.html page.the value is mentioned in count page.
    #key names are taken at random
def about(request):
    return render(request,'about.html')
