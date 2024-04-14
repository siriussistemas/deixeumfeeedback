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
        summary = self.get_queryset().values("type").annotate(count=Count("type"))

        summary = list(summary)

        total_count = sum(item["count"] for item in summary)

        types = ["IDEA", "OTHER", "ISSUE"]
        map_types_count = {}
        for index, type in enumerate(types):
            if type not in map_types_count:
                map_types_count[type] = 0

            if index <= (len(summary) - 1):
                filter = summary[index]
                if filter["type"] in map_types_count:
                    map_types_count[type] = filter["count"]
                else:
                    map_types_count[filter["type"]] = filter["count"]

        response = [
            {"type": "ALL", "count": total_count},
            {"type": "IDEA", "count": map_types_count.get("IDEA")},
            {"type": "OTHER", "count": map_types_count.get("OTHER")},
            {"type": "ISSUE", "count": map_types_count.get("ISSUE")},
        ]

        return Response(data=response, status=status.HTTP_200_OK)
