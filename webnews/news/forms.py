from django import forms
from django.forms import TextInput, Textarea, ModelChoiceField, ClearableFileInput

from .models import News, Comment, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên danh mục....'}),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News

        fields = ('title', 'category', 'description', 'detail', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'}),
            #'category': forms.ModelChoiceField(queryset=Category.objects.all(), required=False,
                                            #  widget=forms.Select(attrs={'class': 'form-control'})),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Nội Dung Chính Về Tin Tức....'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'comment': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Bình Luận Về Tin Tức....'}),
        }
    # name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    # comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'input', 'placeholder': 'Comment'}))
