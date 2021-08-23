from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm


class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book


class BookCreate(CreateView, SuccessMessageMixin):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:book_list')
    success_message = 'Book created'


class BookUpdate(SuccessMessageMixin, UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    form_class = BookForm
    seccess_url = reverse_lazy('books:book_list')
    success_message = 'Book updated'


class BookDelete(SuccessMessageMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book_list')
    success_message = 'Book deleted'
