from django.shortcuts import render
def home(request,user,user1,user2):
    context = {
        'name':user,
        'Roll':user1,
        'age':user2
    }
    
    
    return render(request, 'home.html', context)