from django.urls import path, re_path, include

from . import views
from . import api
from . import views

apipatterns = [
    path('', api.index, name='ars-api'),
    re_path(r'^submit/?$', api.submit, name='ars-submit'),
    re_path(r'^messages/?$', api.messages, name='ars-messages'),
    re_path(r'^agents/?$', api.agents, name='ars-agents'),
    re_path(r'^actors/?$', api.actors, name='ars-actors'),
    re_path(r'^channels/?$', api.channels, name='ars-channels'),
    path('agents/<name>', api.get_agent, name='ars-agent'),
    path('messages/<uuid:key>', api.message, name='ars-message'),
    re_path(r'^status/?$', api.status, name='ars-status'),
]



urlpatterns = [
    path(r'', api.api_redirect, name='ars-base'),
    path(r'app/', views.app_home, name='ars-app-home'),
    path(r'app/status', views.status, name='ars-app-status'),
    path(r'api/', include(apipatterns)),
    path(r'answer/<uuid:key>', views.answer, name='ars-answer'),
]
