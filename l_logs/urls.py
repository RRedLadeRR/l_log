from django.urls import path

from . import views

app_name = 'l_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics list
    path('topics/', views.topics, name='topics'),
    # Current topic info page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new post
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # Page for edit posts
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]