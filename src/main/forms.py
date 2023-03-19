from django import forms
from .models import Reservation
from phonenumbers import COUNTRY_CODE_TO_REGION_CODE


# create a list of tuples for country codes, sorted by code number
COUNTRY_CODES = sorted([(str(code), f"+{code}") for code in COUNTRY_CODE_TO_REGION_CODE.keys()])


class ReservationForm(forms.ModelForm):
    confirm_email = forms.EmailField(label='Confirm Email')
    country_code = forms.ChoiceField(choices=COUNTRY_CODES, required=True, label='Country Tel. Code')

    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email', 'confirm_email', 'country_code', 'mobile_number']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirm_email')
        mobile_number = cleaned_data.get('mobile_number')
        country_code = cleaned_data.get('country_code')

        if email != confirm_email:
            raise forms.ValidationError('Emails do not match')

        # prepend country code to mobile number
        cleaned_data['mobile_number'] = f"{country_code}{mobile_number}"
        return cleaned_data

    def save(self, commit=True):
        reservation = super().save(commit=False)
        # add any additional processing or validation here
        if commit:
            reservation.save()
        return reservation
