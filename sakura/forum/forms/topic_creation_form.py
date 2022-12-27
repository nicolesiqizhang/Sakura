from django import forms


class TopicCreationForm(forms.Form):
    topic_name = forms.CharField(max_length=200)
    topic_description = forms.CharField(widget=forms.Textarea)

    def clean_topic_name(self):
        return self.cleaned_data['topic_name']
