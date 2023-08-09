from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django import forms
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import BookSearchForm
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import redirect

class HomeView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'library/home.html'
    context_object_name = 'books'
    login_url = 'login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Aggregating data for KPIs
        context['total_books'] = Book.objects.count()
        context['total_authors'] = Book.objects.values('author').distinct().count()
        context['total_publications'] = Book.objects.values('publication_date').distinct().count()

         # Get top author by the maximum number of books written
        top_author = Book.objects.values('author').annotate(num_books=Count('id')).order_by('-num_books').first()
        if top_author:
            context['top_author_name'] = top_author['author']
            context['top_author_num_books'] = top_author['num_books']
            context['top_author_prc'] = int(context['top_author_num_books']/context['total_books']*100)
        return context

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    login_url = 'login/'
    paginate_by = 10  # Number of items per page

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(isbn__icontains=query)
            )
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = BookSearchForm(self.request.GET)
        return context
    
class MyBookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'library/my_book_list.html'
    context_object_name = 'books'
    login_url = 'login/'
    paginate_by = 10  # Number of items per page

    def get_queryset(self):
        query = self.request.GET.get('query')
        user = self.request.user  # Get the current logged-in user
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(isbn__icontains=query),
                added_by=user  # Filter by the current user
            )
        return Book.objects.filter(added_by=user)  # Filter by the current user


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = BookSearchForm(self.request.GET)
        return context

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'publication_date', 'isbn', 'cover_image']
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:book_list')
    login_url = 'login/'
    widgets = {
        'publication_date': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}),
    }
    def form_valid(self, form):
        # Set the added_by field to the currently logged-in user
        form.instance.added_by = self.request.user
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('library:home')
        return super(CustomLoginView, self).dispatch(request, *args, **kwargs)

class CustomLogoutView(LogoutView):
    next_page = '/'

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add the email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomRegisterView(FormView):
    form_class = CustomUserCreationForm  # Use your custom form
    template_name = 'registration/register.html'
    success_url = reverse_lazy('library:book_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

def update_book(request, book_id):
    # Handle updating the book object
    return JsonResponse({'success': True})

def delete_book(request, book_id):
    # Handle deleting the book object
    return JsonResponse({'success': True})
