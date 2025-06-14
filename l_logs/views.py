from django.shortcuts import render, redirect

from .forms import TopicForm, EntryForm
from .models import Topic

# Create your views here.

def index(request):
    """App main page"""
    return render(request, 'l_logs/index.html')

def topics(request):
    """Shows topics list"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, 'l_logs/topics.html', context)

def topic(request, topic_id):
    """Shows current topic and all its items"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {
        'topic': topic,
        'entries': entries,
    }
    return render(request, 'l_logs/topic.html', context)

def new_topic(request):
    """Adding new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('l_logs:topics')
    
    context = {"form": form}
    return render(request, 'l_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Adding new post to selected topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('l_logs:topic', topic_id=topic_id)
    
    context = {
        'topic': topic,
        'form': form,
    }
    return render(request, 'l_logs/new_entry.html', context)