from django.urls import path
from optimizationapp import views

app_name="optimization"

urlpatterns = [
    path("", views.optimize, name="optimization"),
    
]
