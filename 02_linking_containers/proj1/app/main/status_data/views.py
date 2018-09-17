from django.http.response import JsonResponse
from status_data.models import Status


def status_view(request):
    if request.method == "POST":
        Status.objects.create(
            app=request.POST.get("app"),
            sensor=request.POST.get("sensor"),
            value=request.POST.get("value")
        )
        return JsonResponse({"saved": True})
    if request.method == "GET":
        return JsonResponse({
            "data": [i.to_dict()
                     for i in Status.objects.order_by("-created_at")]
        })
