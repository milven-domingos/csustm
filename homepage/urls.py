from django.urls import path

from homepage.views import *

urlpatterns = [
    path("", index, name="homepage"),
    # path("account/", include("account.urls")),
]