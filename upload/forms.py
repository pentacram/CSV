from django import forms
from upload.models import UploadByteModel

class UploadFileForm(forms.ModelForm):
    csv_file = forms.FileField()
    class Meta:
        model = UploadByteModel
        fields = ['csv_file']