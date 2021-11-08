from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'editor'

urlpatterns = [
    path('', login_required(views.editor), name="editor"),
    path('api/save-file/', login_required(views.save_file), name="save-file")
]
