from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from patients.forms import ClinicalForm
from patients.models import Patient


class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "patients/patient_list.html"


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = "patients/create_patient.html"
    success_url = reverse_lazy("patient-list")
    fields = "__all__"


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = "patients/update_patient.html"
    success_url = reverse_lazy("patient-list")
    fields = "__all__"


class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "patients/delete_patient.html"
    success_url = reverse_lazy("patient-list")


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = "patients/view_patient.html"
    context_object_name = "patient"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = self.object
        clinical_data = patient.clinicaldata_set.all().order_by("-measuredDateTime")

        context["clinical_data"] = clinical_data

        recent_clinical = clinical_data.filter(
            height__isnull=False, weight__isnull=False
        ).first()

        if recent_clinical:
            height = recent_clinical.height
            weight = recent_clinical.weight
            if height > 0:
                bmi = weight / ((height / 100) ** 2)
                context["bmi"] = round(bmi, 2)
        return context


@login_required
def add_clinical_data(request, **kwargs):
    patient = get_object_or_404(Patient, pk=kwargs["pk"])
    if request.method == "POST":
        form = ClinicalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patient-list")
    else:
        form = ClinicalForm()

    return render(
        request, "patients/clinical_data.html", {"form": form, "patient": patient}
    )
