from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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
        voted_topics = []
        for topic in topic_list:
            if topic.likes.filter(id=1).exists():
                voted_topics.append(topic.id)
        creation_form = TopicCreationForm()
        context = {'topic_list': topic_list, 'creation_form': creation_form,
                   'voted_topics': voted_topics}
        return render(request, 'forum/list_topics.html', context)


def like_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    default_customer = get_object_or_404(Customer, pk=1)
    liked = False
    if topic.likes.filter(id=default_customer.id).exists():
        topic.likes.remove(default_customer)
    else:
        topic.likes.add(default_customer)
        liked = True

    topic.save()
    topic_list = Topic.objects.all()
    creation_form = TopicCreationForm()
    context = {'topic_list': topic_list, 'creation_form': creation_form,
               "topic_id": topic_id,
               "liked": liked}
    # return render(request, 'forum/list_topics.html', context)
    return HttpResponseRedirect(reverse('list_topics'))


def list_topic_threads(request, topic_id):
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
