from django import forms

from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'pages', 'description', 'premiere', 'image')
        ordering = ['title', 'author', 'pages', 'description', 'premiere', 'image']
        labels = {
            'title': 'title',
            'author': 'author',
            'pages': 'pages',
            'description': 'description',
            'premiere': 'premiere',
            'image': 'image'
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control col-4 bg-danger '
        }
        self.fields['author'].widget.attrs = {
            'class': 'form-control col-4 bg-danger',
        }
        self.fields['pages'].widget.attrs = {
            'class': 'form-control col-4 bg-danger'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control col-4 bg-danger'
        }
        self.fields['premiere'].widget.attrs = {
            'class': 'form-control col-4 bg-danger'
        }
        self.fields['image'].widget.attrs = {
            'class': 'form-control col-4 bg-danger'
        }
