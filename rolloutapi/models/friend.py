from django.db import models


class Friend(models.Model):
    r_user_sending = models.ForeignKey(
        "RolloutUser", on_delete=models.CASCADE, related_name="friends")
    r_user_recieving = models.ForeignKey(
        "RolloutUser", on_delete=models.CASCADE, related_name="friends_requests")
    is_approved = models.BooleanField(default=False)
