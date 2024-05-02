from django.shortcuts import render , redirect
from .forms import CategoryForm
# Create your views here.
def add_categorys(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('show_task')
    else:
        form = CategoryForm()
    return render(request, 'category/add_category.html' , {'form' : form})