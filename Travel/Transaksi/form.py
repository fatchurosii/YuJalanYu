from django import forms
from .models import modelTransaksi

class TransaksiForm(forms.ModelForm):
    """Form definition for Transaksi."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paket'].widget= forms.HiddenInput()

    class Meta:
        """Meta definition for Transaksiform."""
        model = modelTransaksi
        fields = "__all__"


