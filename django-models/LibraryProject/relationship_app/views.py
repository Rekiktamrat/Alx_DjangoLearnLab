from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


# Function-Based View: List all books
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })


# Class-Based View: Library Detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Login View
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'


# Logout View
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


# Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})