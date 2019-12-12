from django.contrib import admin
from django.urls import path, include

import eventex.core.views

urlpatterns = [
    path('', eventex.core.views.home, name='home'),
    path('inscricao/', include('eventex.subscriptions.urls')),
    path('palestras/', eventex.core.views.talk_list, name='talk_list'),
    path('palestrantes/<slug:slug>/', eventex.core.views.speaker_detail, name='speaker_detail'),
    path('admin/', admin.site.urls),
]
