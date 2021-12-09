
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from app.models import Todo
from app.serializers import TodoSerializer

# Create your views here.

@api_view(['GET'])
def todo_list(request):
    tarefas = Todo.objects.all()
    json_arq = TodoSerializer(tarefas, many=True)
    return Response(json_arq.data)

@api_view(['POST'])
def todo_post(request):
    json_arq = TodoSerializer(data=request.data)
    if json_arq.is_valid():
        json_arq.save()
        return Response(json_arq.data, status=status.HTTP_201_CREATED)
    return Response(json_arq.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def todo_byId(request, id):
    try:
        tarefa = Todo.objects.get(pk=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    json_arq = TodoSerializer(tarefa)
    return Response(json_arq.data)

@api_view(['DELETE'])
def todo_del(request, id):
    try:
        tarefa = Todo.objects.get(pk=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    tarefa.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def todo_update(request, id):
    try:
        tarefa = Todo.objects.get(pk=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    json_arq = TodoSerializer(tarefa, data=request.data)
    if json_arq.is_valid():
        json_arq.save()
        return Response(json_arq.data)
    return Response(status=status.status.HTTP_400_BAD_REQUEST)
