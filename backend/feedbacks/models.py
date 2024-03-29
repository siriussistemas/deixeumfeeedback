from django.db import models

from users.models import User


class Feedback(models.Model):
    class FeedbackType(models.TextChoices):
        ISSUE = "ISSUE", "Issue"
        IDEA = "IDEA", "Idea"
        OTHER = "OTHER", "Other"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    page = models.URLField(max_length=1000)
    text = models.TextField(max_length=1000)
    type = models.CharField(max_length=10, choices=FeedbackType.choices)
    device = models.CharField(max_length=1000)
    fingersprint = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.text}"
