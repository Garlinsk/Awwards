from django.conf import settings
from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^search/', views.search_projects, name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
