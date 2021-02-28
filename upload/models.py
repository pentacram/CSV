from django.db import models

class UploadByteModel(models.Model):
    file_byte= models.BinaryField()
