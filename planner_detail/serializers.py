from rest_framework import serializers
from .models import Planner

class CellSerializer(serializers.Serializer):
    status = serializers.IntegerField(default=0)
    place_id = serializers.CharField(default = "")
    memo = serializers.CharField(default = "")

class DaySerializer(serializers.Serializer):
    day = CellSerializer(many=True)


class PlannerSerializer(serializers.ModelSerializer):
    cells = DaySerializer(many=True, required=False, default = [{'day': [{'status': 0, 'place_id': '', 'memo': ''}]}])

    class Meta:
        model = Planner
        fields = ['user_id', 'title', 'cells', 'planner_id']