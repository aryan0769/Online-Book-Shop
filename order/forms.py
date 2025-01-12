from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    # List of all Indian states
    DIVISION_CHOICES = (
        
        ('Bihar', 'Bihar'),
        ('Jharkhand', 'Jharkhand'),
        ('West Bengal', 'West Bengal'),
       
    )

    # District Choices for Jharkhand and West Bengal
    DISTRICT_CHOICES = (
        # Jharkhand Districts
        ('Bokaro', 'Bokaro'),
        ('Chatra', 'Chatra'),
        ('Deoghar', 'Deoghar'),
        ('Dhanbad', 'Dhanbad'),
        ('Dumka', 'Dumka'),
        ('East Singhbhum', 'East Singhbhum'),
        ('Garhwa', 'Garhwa'),
        ('Giridih', 'Giridih'),
        ('Godda', 'Godda'),
        ('Gumla', 'Gumla'),
        ('Hazaribagh', 'Hazaribagh'),
        ('Jamtara', 'Jamtara'),
        ('Khunti', 'Khunti'),
        ('Koderma', 'Koderma'),
        ('Latehar', 'Latehar'),
        ('Lohardaga', 'Lohardaga'),
        ('Pakur', 'Pakur'),
        ('Palamu', 'Palamu'),
        ('Ranchi', 'Ranchi'),
        ('Sahibganj', 'Sahibganj'),
        ('Seraikela-Kharsawan', 'Seraikela-Kharsawan'),
        ('Simdega', 'Simdega'),
        ('West Singhbhum', 'West Singhbhum'),

        # West Bengal Districts
        ('Alipurduar', 'Alipurduar'),
        ('Bankura', 'Bankura'),
        ('Bardhaman', 'Bardhaman'),
        ('Birbhum', 'Birbhum'),
        ('Cooch Behar', 'Cooch Behar'),
        ('Dakshin Dinajpur', 'Dakshin Dinajpur'),
        ('Darjeeling', 'Darjeeling'),
        ('Hooghly', 'Hooghly'),
        ('Howrah', 'Howrah'),
        ('Jalpaiguri', 'Jalpaiguri'),
        ('Jhargram', 'Jhargram'),
        ('Kalimpong', 'Kalimpong'),
        ('Koch Bihar', 'Koch Bihar'),
        ('Malda', 'Malda'),
        ('Murshidabad', 'Murshidabad'),
        ('Nadia', 'Nadia'),
        ('North 24 Parganas', 'North 24 Parganas'),
        ('Purba Medinipur', 'Purba Medinipur'),
        ('Purulia', 'Purulia'),
        ('South 24 Parganas', 'South 24 Parganas'),
        ('West Medinipur', 'West Medinipur'),
        ('Kolkata', 'Kolkata'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('UPI', 'Unified Payments Interface (UPI)'),
        ('Paytm', 'Paytm'),
        ('PhonePe', 'PhonePe'),
        ('Google Pay', 'Google Pay'),
        ('Amazon Pay', 'Amazon Pay'),
    )

    division = forms.ChoiceField(choices=DIVISION_CHOICES)
    district = forms.ChoiceField(choices=DISTRICT_CHOICES)
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']