from django.urls import path

from . import views

urlpatterns = [
    path("", views.PatientListView.as_view(), name="patient-list"),
    path("view/<int:pk>", views.PatientDetailView.as_view(), name="view_patient"),
    path("add/<int:pk>", views.add_clinical_data, name="clinical_data"),
    path("update/<int:pk>", views.PatientUpdateView.as_view(), name="update_patient"),
    path("delete/<int:pk>", views.PatientDeleteView.as_view(), name="delete_patient"),
    path("create/", views.PatientCreateView.as_view(), name="create_patient"),
]
