from django.db import models


class Friend(models.Model):
    r_user_sending = models.ForeignKey("RolloutUser", on_delete=models.CASCADE)
    r_user_recieving = models.ForeignKey(
        "RolloutUser", on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
