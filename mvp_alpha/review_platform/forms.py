from django import forms
from .models import Book, Genre


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    GENRE_OPTIONS = [
        ('FICTION', 'Fiction'),
        ('NON-FICTION', 'Non-Fiction'),
        ('AUTOBIOGRAPHY', 'Autobiography'),
        ('NOVELS', 'Novels'),
        ('THRILLERS', "Thrillers"),
        ('HISTORY', 'History'),
        ('POETRY', 'Poetry'),
    ]

    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'select2'}),
    )

class ReviewForm(forms.Form):
    rating = forms.FloatField(
    min_value=1, 
    max_value=5,
    help_text='The rating score must be between 1 and 5, and can only be in increments of 0.5.'
    )
    
    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if (rating * 2) % 1 != 0:
            raise forms.ValidationError('The rating score must be in increments of 0.5.')
        
    review = forms.CharField(widget=forms.Textarea)    