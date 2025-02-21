from django.urls import path
from .views import AppView


urlpatterns = [
    # CRUD operations for apps
    path('', AppView.as_view(), name='app-list-create'),
    path('<int:pk>/', AppView.as_view(), name='app-retrieve-update-delete'),
]
