from django.conf.urls import include, url
from django.contrib import admin

from eventex.core.views import home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^inscricao/', include('eventex.subscriptions.urls',
                                namespace='subscriptions')),
    url(r'^admin/', admin.site.urls),
]
