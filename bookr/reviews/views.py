from django.shortcuts import get_object_or_404, render
from .models import Book, Review, Contributor
from .utils import average_rating
from .forms import SearchForm


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for
                                          review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,
                          'book_rating': book_rating,
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

    return render(request, 'reviews/book_details.html', context)


def index(request):
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set()
    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            contributors = Contributor.objects.filter(first_names__icontains=search) |\
                Contributor.objects.filter(last_names__icontains=search)
            for contributor in contributors:
                for book in contributor.book_set.all():
                    books.add(book)
    return render(request, "reviews/search-results.html",
                  {"form": form, "search_text": search_text,
                   "books": books})
