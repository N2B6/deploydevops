"""
Form for creating or updating WanderlustUser instances.
"""
from django import forms
from .models import WanderlustUser, Trip  # import specific models instead of using wildcard import

class WanderlustUserForm(forms.ModelForm):
    """
     Form for creating or updating WanderlustUser instances.
    """
    class Meta:
        """
        Metadata for WanderlustUserForm.
        """
        model = WanderlustUser
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'phone_number', 'dob']

    def __init__(self, *args, **kwargs):
        """
        Initializer for WanderlustUserForm.
        """
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        Save method for WanderlustUserForm.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_username(self):
        """
        Custom validation for username field.
        """
        username = self.cleaned_data['username']
        # Add custom validation logic if needed
        return username


class Addtrip(forms.ModelForm):
    """
     Form for adding a trip.
    """
    class Meta:
        """
        Metadata for AddTripForm.
        """
        model = Trip
        fields = ['title', 'destination', 'description', 'start_date', 'end_date', 'travel_mode',
                  'accommodation_type', 'estimated_budget', 'image', 'max_participants']
        exclude = ['participants', 'created_at', 'updated_at', 'user']

# end
