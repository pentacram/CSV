from django.forms import ModelForm
from upload.models import UploadByteModel

class UploadFileForm(ModelForm):
    class Meta:
        model = UploadByteModel
        fields = ['csv_file']