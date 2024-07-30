from django.shortcuts import render, redirect

# Create your views here.
def list_tasks(request):
    return render(request, 'tasks/template/list_tasks.html')



