from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Book
from .forms import BookForm


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),
                                    self.get_login_url(),
                                    self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class BookList(ListView):
    model = Book
    template_name = 'books/book_list.html'


class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreate(UserAccessMixin, CreateView, SuccessMessageMixin):
    permission_required = 'books.add_book'

    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:book_list')
    success_message = 'Book created'

"""
Fields for 'Access Mixins':
    login_url = settings.LOGIN_URL
    raise_exception = False
    redirect_field_name = REDIRECT_FIELD_NAME
    redirect_unauthenticated_users = False
"""

class BookUpdate(UserAccessMixin, UpdateView, SuccessMessageMixin):
    permission_required = 'books.change_book'

    model = Book
    template_name = 'books/book_form.html'
    form_class = BookForm
    seccess_url = reverse_lazy('books:book_list')
    success_message = 'Book updated'


class BookDelete(UserAccessMixin, DeleteView, SuccessMessageMixin):
    permission_required = 'books.delete_book'

    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book_list')
    success_message = 'Book deleted'