from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render, redirect
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer
from .forms import CompanyForm, VacancyForm


# List all companies and create a new company
@api_view(["GET", "POST"])
def company_list_fbv(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update, or delete a single company
@api_view(["GET", "PUT", "DELETE"])
def company_detail_fbv(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# List all vacancies and create a new vacancy
@api_view(["GET", "POST"])
def vacancy_list_fbv(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update, or delete a single vacancy
@api_view(["GET", "PUT", "DELETE"])
def vacancy_detail_fbv(request, pk):
    try:
        vacancy = Vacancy.objects.get(pk=pk)
    except Vacancy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = VacancySerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# List vacancies by company
@api_view(["GET"])
def company_vacancies_fbv(id):
    vacancies = Vacancy.objects.filter(company_id=id)
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)


class CompListCBV(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer  # using our Serializer


class CompDetCBV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class VacListCBV(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer  # using ModelSerializer


class VacDetCBV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class CompVacCBV(generics.ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        company_id = self.kwargs.get("id")
        return Vacancy.objects.filter(company_id=company_id)


class Top10Vac(generics.ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.order_by("-salary")[:10]


def main_view(request):
    return render(request, "main.html")


def add_entries(request):
    company_form = CompanyForm()
    vacancy_form = VacancyForm()

    if request.method == "POST":
        # Check which form was submitted
        if "submit_company" in request.POST:
            company_form = CompanyForm(request.POST)
            if company_form.is_valid():
                company_form.save()
                return redirect("add_entries")  # Redirect back to clear the form
        elif "submit_vacancy" in request.POST:
            vacancy_form = VacancyForm(request.POST)
            if vacancy_form.is_valid():
                vacancy_form.save()
                return redirect("add_entries")

    context = {
        "company_form": company_form,
        "vacancy_form": vacancy_form,
    }
    return render(request, "add_entries.html", context)
