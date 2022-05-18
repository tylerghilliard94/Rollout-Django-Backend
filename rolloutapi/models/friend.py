from django.db import models


class Friend(models.Model):
    requester = models.ForeignKey("RolloutUser", on_delete=models.CASCADE)
    requestee = models.ForeignKey("RolloutUser", on_delete=models.CASCADE)
