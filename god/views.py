from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def bookList(request):  
    books = Book.objects.all().order_by('year')  
    return render(request,"book-list.html",{'books':books})  

def bookCreate(request):  
    form = BookForm()
    if request.method == "POST":  
        form = BookForm(request.POST)  
        if form.is_valid():  
                form.save() 
                form = BookForm()
                return redirect('book-list')  
    return render(request,'book-create.html',{'form':form})  

def bookUpdate(request, id):  
    book = Book.objects.get(id=id)
    form = BookForm()
    if request.method == "POST":  
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():  
                form.save() 
                return redirect('/book-list')  
    return render(request,'book-update.html',{'form':form})  

def bookDelete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book-list')