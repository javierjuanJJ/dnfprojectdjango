from rest_framework.views import APIView
from rest_framework.response import Response

from dfrapp.models import Student
from dfrapp.serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated

class TextView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        student1 = qs.first()
        #serializer = StudentSerializer(qs, many=True)
        serializer = StudentSerializer(student1)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)