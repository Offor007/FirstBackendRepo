from django import forms
from .models import Comment




class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, min_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email= forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    website=forms.URLField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    
class ReaderCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields= ["name", "email", "website", "comment", "image" ]
        widgets={
            "name":forms.TextInput(attrs={'class': 'form-control'}),
            "email":forms.TextInput(attrs={'class': 'form-control'}),
            "website":forms.TextInput(attrs={'class': 'form-control'}),
            "comment":forms.Textarea(attrs={'class': 'form-control'}),
            "image":forms.FileInput(attrs={'class': 'form-control'})
        }