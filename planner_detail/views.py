from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import IntegrityError
from django.utils.crypto import get_random_string

from .models import Planner
from planner_detail.serializers import PlannerSerializer, DaySerializer

PLANNER_ID_SIZE = 20

#create new planner
@api_view(['POST'])
def create_Planner(request):
    #planner_id 생성
    planner_id = get_random_string(length=PLANNER_ID_SIZE)
    request.data["planner_id"] = planner_id

    #검정 이후 저장
    serializer = PlannerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

#read Planner
@api_view(['GET'])
def get_Planner(request, planner_id):
    try:
        planner = Planner.objects.get(planner_id=planner_id)
    except Planner.DoesNotExist:
        return Response(status=404)

    serializer = PlannerSerializer(planner)
    return Response(serializer.data)

#read all Planner
@api_view(['GET'])
def get_AllPlanner(request):
    try:
        planner = Planner.objects.all()
    except Planner.DoesNotExist:
        return Response(status=404)

    serializer = PlannerSerializer(planner, many=True)
    return Response(serializer.data)


#update planner
@api_view(['PUT'])
def update_Planner(request, planner_id):
    #try to find Planner
    try:
        planner = Planner.objects.get(planner_id=planner_id)

    except Planner.DoesNotExist:
        return Response(status=404)
    
    #기존 planner 객체를 instance로 전달 이후 data로 업데이트
    serializer = PlannerSerializer(instance=planner, data=request.data, partial=True) #업데이트 필요한 데이터만 업데이트하기위해 partial=True 넣음
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=201)
    else:
        print(serializer.data)
        return Response(serializer.data, status=400)    

#delete planner
@api_view(['DELETE'])
def delete_Planner(request, planner_id):
    try:
        planner = Planner.objects.get(planner_id=planner_id)

    except Planner.DoesNotExist:
        return Response(status=404)
    
    planner.delete()
    return Response(status=404)
    

