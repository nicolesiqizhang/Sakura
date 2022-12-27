from django.shortcuts import render, get_object_or_404

from .forms.thread_creation_form import ThreadCreationForm
from .forms.topic_creation_form import TopicCreationForm
from .models import Customer
from .models import Thread
from .models import Topic


# Create your views here.
def list_topics(request):
    if request.method == 'POST':
        form = TopicCreationForm(request.POST)
        if form.is_valid():
            new_topic = Topic.create(form.cleaned_data['topic_name'],
                                     form.cleaned_data['topic_description'])
            new_topic.save()

            topic_list = Topic.objects.all()
            creation_form = TopicCreationForm()
            context = {'topic_list': topic_list, 'creation_form': creation_form}
            return render(request, 'forum/list_topics.html', context)
    else:
        topic_list = Topic.objects.all()
        creation_form = TopicCreationForm()
        context = {'topic_list': topic_list, 'creation_form': creation_form}
        return render(request, 'forum/list_topics.html', context)


def list_threads(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form = ThreadCreationForm(request.POST)
        if form.is_valid():
            new_thread = Thread.create(topic,
                                       form.cleaned_data['thread_content'],
                                       Customer.objects.get(pk=1))
            new_thread.save()

    creation_form = ThreadCreationForm()
    context = {'thread_list': topic.thread_set.all(),
               'creation_form': creation_form}
    return render(request, 'forum/list_threads.html', context)
