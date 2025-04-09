import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';
import { Company } from '../models/company';
import { Vacancy } from '../models/vacancy';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-companies',
  imports: [ CommonModule ],
  templateUrl: './companies.component.html',
  styleUrl: './companies.component.css'
})
export class CompaniesComponent implements OnInit {
  companies: Company[] = [];
  vacancies: Vacancy[] = [];
  selectedCompanyId: number | null = null;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getCompanies().subscribe((data) => {
      this.companies = data;
    });
  }

  showVacancies(companyId: number): void {
    this.selectedCompanyId = companyId;
    this.apiService.getCompanyVacancies(companyId).subscribe((data) => {
      this.vacancies = data;
    });
  }
}
