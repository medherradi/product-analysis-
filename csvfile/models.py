from django.db import models
import os
# Create your models here.

class Csv(models.Model):
      file_name = models.FileField(upload_to ='csvfile/', max_length=100)
      uploaded = models.DateTimeField(auto_now_add=True)
      activated = models.BooleanField(default=False)

      def __str__(self):
            return f'File id: {self.id}'
      
      #def filename(self):
      #      self.file_name.name = os.path.basename(self.file_name.name)
      #     return self.file_name.name
