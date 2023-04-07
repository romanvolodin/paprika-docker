from django.urls import path

from shots import views


app_name = "shots"
urlpatterns = [
    path(
        "",
        views.ShotListView.as_view(),
        name="list",
    ),
]
