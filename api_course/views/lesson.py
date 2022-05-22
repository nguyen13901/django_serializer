from rest_framework import viewsets, status
from rest_framework.response import Response

from api_course.serializer import LessonSerializer
from api_course.models import Lesson
from rest_framework.decorators import action


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer

    @action(methods=['post'], detail=True, url_path="hide-lesson")
    def hide_lesson(self, request, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=LessonSerializer(l, context={"request": request}).data,
                        status = status.HTTP_200_OK)