from django.shortcuts import render, redirect

# Create your views here.
def list_tasks(request):
    return render(request, 'lits_tasks.html')



