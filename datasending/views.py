from django.shortcuts import render
def home(request):
    # context = {
    #     'name':user,
    #     'Roll':user1,
    #     'age':user2
    # }
    
    
    return render(request, 'home.html')