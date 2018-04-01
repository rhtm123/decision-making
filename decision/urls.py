from django.conf.urls import url
from decision import views

urlpatterns = [
    url(r'^$', views.DecisionFilter.as_view()),
    url(r'^(?P<pk>[0-9]+)$', views.decision_detail),
    url(r'^points/(?P<pk>[0-9]+)$', views.points),
]