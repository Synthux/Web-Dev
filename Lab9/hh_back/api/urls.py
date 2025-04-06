from django.urls import path
from . import views

urlpatterns = [
    path("companies/", views.CompList.as_view(), name="company-list"),
    path("companies/<int:pk>/", views.CompDetail.as_view(), name="company-detail"),
    path("companies/<int:id>/vacancies/", views.CompVacs.as_view(), name="company-vacancies"),
    path("vacancies/", views.VacList.as_view(), name="vacancy-list"),
    path("vacancies/<int:pk>/", views.VacDetail.as_view(), name="vacancy-detail"),
    path("vacancies/top_ten/", views.Top10Vac.as_view(), name="top-10-vacancies"),
    path("positions/", views.PosList.as_view(), name="position list"),
    path("positions/<int:pk>/", views.PosDetail.as_view(), name="position-detail"),
    path("add/", views.add_entries, name="add_entries"),
]
