from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('author', 'title', 'image', 'text', 'created_date', 'start_date', 'end_date')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 16 * 1024 * 1024:
                raise forms.ValidationError("File too large")
            return image
        else:
            raise forms.ValidationError("Couldn't read uploaded image")