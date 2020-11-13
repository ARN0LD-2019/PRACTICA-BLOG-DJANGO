from django import forms
from .models import Post, Category, Comment

#choices = [('Platillos Fuertes','Platillos Fuertes'), ('Entradas','Entradas'), ('Sin Categoria','Sin Categoria'),]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo del post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titulo del Tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'arnold', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder':'Selecciona tu categoria'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titulo del Post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titulo del Tag'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Descripcion'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tu nombre'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Descripcion'}),
        }