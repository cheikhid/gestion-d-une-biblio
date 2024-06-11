from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from content.models import Book , Category
from content.forms import BookForm, CategoryForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Rediriger vers la page d'accueil après la connexion
    return render(request, 'pages/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige vers la page de connexion après la déconnexion




@login_required
def index(request):
    
    if request.method =='POST':
        add_book = BookForm(request.POST , request.FILES)
        add_category = CategoryForm(request.POST)
        
        if add_category.is_valid():
            add_category.save()
        
        if add_book.is_valid():
            add_book.save()
     
     




    x = {"cat": Category.objects.all(),
         "books" : Book.objects.all(),
         "form":BookForm(),
         "formcat":CategoryForm(),
         "allbooks":Book.objects.filter(active=True).count(),
         "availblebook":Book.objects.filter(status="available").count(),
         "sellbook":Book.objects.filter(status='sell').count(),
         "rentalbook":Book.objects.filter(status='rental').count(),
         
    }
    
    return render(request, 'pages/index.html' ,x)

def books(request):
    
    search =  Book.objects.all()
    title = None
    if 'search_name' in request.GET :
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)



    x = {
        "cat": Category.objects.all(),
         "books" : search,
         "formcat":CategoryForm(),
         }

    return render(request, 'pages/books.html',x)


def update(request, id):
     book_id = Book.objects.get(id = id)
     
     if request.method =="POST":
         update_book = BookForm(request.POST , request.FILES, instance=book_id)
         if update_book.is_valid():
             update_book.save()
             return redirect('/')

     else:
         update_book=BookForm(instance=book_id)

     x = {
         "updatebook":update_book
     }
      
     return render(request, 'pages/update.html',x)


def delete(request, id):
    if request.method == 'POST':
        delete_book = get_object_or_404(Book, id=id)
        delete_book.delete()
        return redirect('/')
    return render(request, "pages/delete.html")