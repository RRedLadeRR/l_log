from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # Add default url for authorization
    path('', include('django.contrib.auth.urls'))
]
