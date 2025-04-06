from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Company, Vacancy, Position
from .serializers import CompSerz, VacSerz, PosSerz
from .forms import CompForm, VacForm, PosForm


def main_view(request):
    return render(request, "main.html")


def add_entries(request):
    comp_form = CompForm()
    vac_form = VacForm()
    pos_form = PosForm()

    if request.method == "POST":
        # Checks which form was submitted
        if "submit_company" in request.POST:
            comp_form = CompForm(request.POST)
            if comp_form.is_valid():
                comp_form.save()
                return redirect("add_entries")  # Redirects back to clear the form
        elif "submit_position" in request.POST:
            pos_form = PosForm(request.POST)
            if pos_form.is_valid():
                pos_form.save()
                return redirect("add_entries")
        elif "submit_vacancy" in request.POST:
            vac_form = VacForm(request.POST)
            if vac_form.is_valid():
                vac_form.save()
                return redirect("add_entries")

    context = {
        "comp_form": comp_form,
        "pos_form": pos_form,
        "vac_form": vac_form,
    }
    return render(request, "add_entries.html", context)


# Company Endpoins


# List of all Companies
class CompList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompSerz


# Get one Company
class CompDetail(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompSerz


# List of Vacancies by Company
class CompVacs(generics.ListAPIView):
    serializer_class = VacSerz

    def get_queryset(self):
        comp_id = self.kwargs.get("id")
        return Vacancy.objects.filter(company_id=comp_id)


# Position Endpoints


# List of all Positions
class PosList(generics.ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PosSerz


# Get one Position
class PosDetail(generics.RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PosSerz


# Vacancies Endpoints


# List of all Vacancies
class VacList(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacSerz


# Get one Vacancy
class VacDetail(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacSerz


# List of top 10 vacancies sorted by decreasing salary
class Top10Vac(generics.ListAPIView):
    serializer_class = VacSerz

    def get_queryset(self):
        return Vacancy.objects.order_by("-salary")[:10]


# List of Positions by Vacancies
class PosVac(generics.ListAPIView):
    serializer_class = PosSerz

    def get_queryset(self):
        pos_id = self.kwargs.get("id")
        return Position.objects.filter(position_id=pos_id)
