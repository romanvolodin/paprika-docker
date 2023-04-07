from django.shortcuts import render
from django.views import View

from shots.models import ShotGroup


class ShotListView(View):
    def get(self, request, *args, **kwargs):
        grouped_shots = {}
        shot_groups = ShotGroup.objects.order_by("title")
        for shot_group in shot_groups:
            grouped_shots[shot_group.title] = shot_group.shots.all()

        return render(request, "shots/shot_list.html", {"grouped_shots": grouped_shots})
