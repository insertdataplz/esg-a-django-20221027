from django.shortcuts import render, redirect
from diary.models import Memory
from diary.forms import MemoryForm

def memory_list(request):
    memory_qs = Memory.objects.all().order_by("-id")
    return render(request, "diary/memory_list.html", {
        'memory_list' : memory_qs
    })

def memory_detail(request, pk):
    memory = Memory.objects.get(pk=pk)
    return render(request, "diary/memory_detail.html", {
        'memory': memory
    })

def memory_new(request):
    if request.method == "GET":
        form = MemoryForm()
    else:
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save()
            return redirect(memory)
    
    return render(request, "diary/memory_form.html", {
        'form': form
    })