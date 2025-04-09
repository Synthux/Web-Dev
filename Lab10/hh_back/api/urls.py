from django.urls import path
from . import views

urlpatterns = [
    # Function-Based URLs
    path('fbv/companies/', views.company_list_fbv, name='company-list-fbv'),
    path('fbv/companies/<int:pk>/', views.company_detail_fbv, name='company-detail-fbv'),
    path('fbv/companies/<int:id>/vacancies/', views.company_vacancies_fbv, name='company-vacancies-fbv'),
    path('fbv/vacancies/', views.vacancy_list_fbv, name='vacancy-list-fbv'),
    path('fbv/vacancies/<int:pk>/', views.vacancy_detail_fbv, name='vacancy-detail-fbv'),

    # Class-Based URLs
    path('cbv/companies/', views.CompListCBV.as_view(), name='company-list-cbv'),
    path('cbv/companies/<int:pk>/', views.CompDetCBV.as_view(), name='company-detail-cbv'),
    path('cbv/companies/<int:id>/vacancies/', views.CompVacCBV.as_view(), name='company-vacancies-cbv'),
    path('cbv/vacancies/', views.VacListCBV.as_view(), name='vacancy-list-cbv'),
    path('cbv/vacancies/<int:pk>/', views.VacDetCBV.as_view(), name='vacancy-detail-cbv'),
    path('cbv/vacancies/top_ten/', views.Top10Vac.as_view(), name='top-ten-vacancies'),
    
    path('add/', views.add_entries, name='add_entries'),
]
