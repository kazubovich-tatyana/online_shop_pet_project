from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('category/<slug:cat_slug>/', views.SaleNewCategoryPage.as_view(), name='show_category'),

]