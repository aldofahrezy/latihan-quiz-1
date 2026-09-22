from django import forms  # noqa: F401
from main.models import Bookmark

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ["label", "url", "priority"]

    def clean_label(self):
        label = self.cleaned_data["label"].strip()
        if len(label) < 3:
            raise forms.ValidationError("Label minimal tiga karakter.")
        return label

    def clean_priority(self):
        priority = self.cleaned_data["priority"]
        if priority > 10:
            raise forms.ValidationError("Prioritas maksimal 10.")
        return priority