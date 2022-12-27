from django import forms


class ThreadCreationForm(forms.Form):
    thread_content = forms.CharField(widget=forms.Textarea)

    def clean_thread_content(self):
        return self.cleaned_data['thread_content']
