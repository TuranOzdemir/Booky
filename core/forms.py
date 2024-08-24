from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review
from django import forms
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length="50", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="",max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<ul class="form-text text-muted"><li>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</li><li>Your username must be unique</li></ul>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted"><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Enter the same password as before, for verification.</span>'


class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control'}))
    book_rating = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating'}))

    class Meta:
        model = Review
        fields = ['review_text', 'book_rating']
        

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['review_text'].widget.attrs['rows'] = 4
        self.fields['review_text'].label = ''
        self.fields['review_text'].widget.attrs['placeholder'] = 'Write your review here...'
        self.fields['review_text'].widget.attrs['class'] = 'form-control'
        
        self.fields['review_text'].help_text = '<span class="form-text text-muted">Write your review here...</span>'

        self.fields['book_rating'].widget.attrs['placeholder'] = 'Rating'
        self.fields['book_rating'].widget.attrs['class'] = 'form-control'
        self.fields['book_rating'].widget.attrs['min'] = 1
        self.fields['book_rating'].widget.attrs['max'] = 5
        self.fields['book_rating'].label = ''
        
    
