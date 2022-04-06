#from django.shortcuts import render
#from django.shortcuts import render_to_response
from students.models import Student as stm
from rest_framework import generics
from students.serializers import StudentSerializer as sts

from rest_framework import status, views
from rest_framework.response import Response

"""
def principal(request):
    students = stm.objects.all()
    return render_to_response("index.html", {'alumnos':students})
"""


class StudentList(generics.ListCreateAPIView):
    serializer_class = sts
    queryset = stm.objects.all()
"""
class StudentList(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = sts(data=request.data)
        serializer.save()
                
        return Response(status=status.HTTP_201_CREATED)
"""

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = sts
    queryset = stm.objects.all()

