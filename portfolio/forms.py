from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["full_name", "email", "subject", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your email address"}),
            "subject": forms.TextInput(attrs={"placeholder": "Message subject"}),
            "message": forms.Textarea(
                attrs={"placeholder": "Tell me about your opportunity...", "rows": 5}
            ),
        }