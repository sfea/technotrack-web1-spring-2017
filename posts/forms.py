from django import forms

from posts.models import Blog, Post


class SortForm(forms.Form):

    sort = forms.ChoiceField(
        choices=(
            ('updated_at', u'Date'),
            ('title', u'Title'),
            ('rate', u'Rate'),
            ('description', u'Description'),
        ),
        required=False
    )
    search = forms.CharField(required=False)


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'description', 'rate')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'rate')