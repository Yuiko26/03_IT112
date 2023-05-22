from django.shortcuts import get_object_or_404, render
from .models import Book, Review
from .utils import average_rating
from .forms import ExampleForm, SearchForm

def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for \
                                          review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,\
                          'book_rating': book_rating,\
                          'number_of_reviews': number_of_reviews})
    context = {
        'book_list': book_list
    }
    return render(request, 'reviews/books_list.html', context)

def details(request, pk):
    details_book = get_object_or_404(Book, pk=pk)
    details_review = details_book.review_set.all() 
    book_rating = average_rating([review.rating for review in details_review])
    context = {
        'book_id': pk,
        'details_book': details_book,
        'reviews': details_review, 
        'rating': book_rating, 
    }

    return render( request, 'reviews/book_details.html',context)

def index(request):
    return render(request, "base.html")

