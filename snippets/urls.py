from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from snippets import views

schema_view = get_schema_view(title='Pastebin API')
admin.autodiscover()

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('schema/', schema_view),
]



