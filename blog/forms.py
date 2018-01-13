from django import forms
from .models import Comment


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Temat')
    email = forms.EmailField(required=True, label='Adres e-mail')
    message = forms.CharField(widget=forms.Textarea, label='Treść')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

Category_choice=[('travels', 'Travels'), ('fun','Fun'),('lifestyle', 'Lifestyle'), ('thoughts', 'Thoughts')]


class CategoryForm(forms.ModelForm):
    widget=forms.Select(choices=Category_choice)