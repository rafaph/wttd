from django.urls import path

import eventex.subscriptions.views

app_name = 'subscriptions'

urlpatterns = [
    path('', eventex.subscriptions.views.new, name='new'),
    path('<uuid:pk>/', eventex.subscriptions.views.detail, name='detail'),
]
