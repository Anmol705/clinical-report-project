from allauth.account.forms import SignupForm
from django import forms

from patients.models import ClinicalData, Patient, UserProfile


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    phone_number = forms.CharField(min_length=10, max_length=10, label="Phone Number")
    designation = forms.ChoiceField(
        choices=[("patient", "Patient"), ("doctor", "Doctor"), ("admin", "Admin")]
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()

        phone_number = self.cleaned_data["phone_number"]
        designation = self.cleaned_data["designation"]
        UserProfile.objects.create(
            user=user, phone_number=phone_number, designation=designation
        )

        return user


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class ClinicalForm(forms.ModelForm):
    class Meta:
        model = ClinicalData
        fields = "__all__"
