from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(
        max_length=500,
        label="Izoh",
        widget=forms.TextInput(
            attrs={
                "style": "width: 100%; border-radius: 20px; padding: 20px; margin: 10px",
                "placeholder": "Izoh matni"
            }
        )
    )

    class Meta:
        model = Comment
        fields = ["text"]
