from django.db import models

class UploadByteModel(models.Model):
    csv_file = models.FileField()
    file_byte= models.BinaryField()
