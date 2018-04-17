from django.urls import path

from admin_dashboard.views import *

urlpatterns = [
    path("", dashboard, name="dashboard"),
    # path("account/", include("account.urls")),
]