from typing import ItemsView
from django import forms
from .models import Post, Category


#choices=[('codoing','coding'),('sports','sports'),('entertainment','entertainment'),]
choices = Category.objects.all().values_list('name','name')

choice_list=[]

for items in choices:
    choice_list.append(items)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','author','category','body')
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'A nice title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder': 'Bucket this blog'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body')
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'A nice title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder': 'Bucket this blog'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }     