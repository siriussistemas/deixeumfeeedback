from rest_framework import serializers
from ..models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("id", "text", "fingersprint", "device", "created_at", "page", "type")
        ordering = ["-created_at"]
