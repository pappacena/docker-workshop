import json
from django.http.response import JsonResponse
from status_data.models import Status


def status_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Status.objects.create(
            app=data.get("app"),
            sensor=data.get("sensor"),
            value=data.get("value")
        )
        return JsonResponse({"saved": True})
    if request.method == "GET":
        return JsonResponse({
            "data": [i.to_dict()
                     for i in Status.objects.order_by("-date")]
        })
