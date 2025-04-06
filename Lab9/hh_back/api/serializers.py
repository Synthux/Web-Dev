from rest_framework import serializers
from .models import Company, Vacancy, Position


class CompSerz(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "description", "city", "address"]


class PosSerz(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ["id", "name", "description"]


class VacSerz(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = [
            "id",
            "name",
            "description",
            "salary",
            "company",
            "position",
            "position_id",
        ]
