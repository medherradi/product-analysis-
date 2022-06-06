from django.db import models

# Create your models here.

class Customer(models.Model):
      company_name = models.CharField(max_length=120)
      budget = models.PositiveIntegerField(help_text='en DRH')
      employment = models.PositiveIntegerField()
      joined = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return f'{self.company_name}'
