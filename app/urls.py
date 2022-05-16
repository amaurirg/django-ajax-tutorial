from django.contrib import admin
from django.urls import path

from app.views import AjaxHandlerView

urlpatterns = [
    path('', AjaxHandlerView.as_view()),
]