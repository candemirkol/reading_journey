from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Book, Genre, Wishlist
from .forms import BookAdminForm
import json


def home(request):
    latest_books = Book.objects.all().order_by('-id')[:10] # Can be adjusted
    return render(request, 'review_platform_home.html', {'latest_books': latest_books})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookAdminForm()
    return render(request, 'books/add_book.html', {'form': form})

def genre_books(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    books = Book.objects.filter(genre=genre)
    return render(request, 'books/genre_books.html', {'genre': genre, 'books': books})

@require_POST
@login_required
def add_to_wishlist(request):
    try:
        # Parse the JSON body
        data = json.loads(request.body)
        book_id = data.get('bookId')
        
        # Ensure that book_id is valid
        if not book_id:
            return JsonResponse({'success': False, 'message': 'No book ID provided'}, status=400)
        
        book = get_object_or_404(Book, id=book_id)
        
        # Create or get the wishlist
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist.books.add(book)
        wishlist.save()  # Save the wishlist to ensure the book is added
        
        return JsonResponse({'success': True, 'message': 'Book added to wishlist!'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})

@login_required
def view_wishlist(request):
    # Get or create the wishlist for the user
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'books/wishlist.html', {'wishlist': wishlist})