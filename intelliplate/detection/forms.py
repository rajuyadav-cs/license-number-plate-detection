from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                "class": "w-full rounded-xl border border-slate-700 bg-slate-950 p-3 text-sm text-slate-300"
            }
        )
    )