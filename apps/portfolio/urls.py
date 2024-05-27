from django.urls import path

from apps.portfolio import views

urlpatterns = [
    path("", views.index_view, name='index'),
    path("contact/", views.contact_view, name='contact'),
    path("portfolio/", views.portfolio_view, name='portfolio'),
    path("portfolio/<int:pk>", views.portfolio_detail_view, name='portfolio_detail'),
    path("services/<int:pk>", views.service_detail_view, name='service_detail'),
    # path('inquiry/', views.inquiry_view, name='inquiry'),
    path('switch-language/<str:lang_code>/', views.switch_language, name='switch_language'),
]
