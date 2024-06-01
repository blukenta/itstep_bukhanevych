from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("change", views.change),
    path("create", views.add_todo),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)