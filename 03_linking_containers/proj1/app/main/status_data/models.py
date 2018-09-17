from django.db import models


class Status(models.Model):
    app = models.CharField(max_length=255)
    sensor = models.CharField(max_length=255)
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        data = {k: getattr(self, k) for k in ["app", "sensor", "value"]}
        data["date"] = self.date.isoformat()
        return data
