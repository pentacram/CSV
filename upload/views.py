from django.shortcuts import render, redirect, HttpResponse
import csv
from upload.forms import UploadFileForm
from upload.models import UploadByteModel

def upload_file(request):
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_data = form.save(commit=False)
            uploaded_data.file_byte = form.cleaned_data['csv_file'].file.read()
            uploaded_data.save()
            return redirect('/')
        else:
            return render(request, 'upload.html', {'form': form})
    return render(request, 'upload.html', {'form': form})