from django.shortcuts import render
def home(request,user,user1):
    context = {
        'name':user,
        'Roll':user1,
        'age':19
    }
    
    
    return render(request, 'home.html', context)