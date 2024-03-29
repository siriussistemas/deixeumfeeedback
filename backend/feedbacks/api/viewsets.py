from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from .filters import FeedbacksFilter
from ..models import Feedback
from .serializers import FeedbackSerializer

from rest_framework.decorators import action
from rest_framework import status

from django.db.models import Count

from rest_framework.response import Response


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = FeedbacksFilter

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=["GET"])
    def filters_data(self, request):
        filters_type_count = self.queryset.values("type").annotate(count=Count("type"))
        total_count = sum(item["count"] for item in filters_type_count)

        filters_type_count = list(filters_type_count)
        filters_type_count.insert(0, {"type": "ALL", "count": total_count})

        return Response(data=filters_type_count, status=status.HTTP_200_OK)
