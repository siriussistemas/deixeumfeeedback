from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

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
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=["GET"])
    def filters_data(self, request):
        # TODO: study if use get_queryset is a best pratice or not
        summary = self.get_queryset().values("type").annotate(count=Count("type"))

        summary = list(summary)

        total_count = sum(item["count"] for item in summary)

        type_counts = {}

        for item in summary:
            type_counts[item["type"]] = item["count"]

        types = Feedback.FeedbackType.values

        map_types_count = [
            {"type": type_, "count": type_counts.get(type_, 0)} for type_ in types
        ]

        map_types_count.insert(0, {"type": "ALL", "count": total_count})

        return Response(data=map_types_count, status=status.HTTP_200_OK)
