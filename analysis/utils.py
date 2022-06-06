from django.contrib.auth.models import User 

def get_salesman_name(val):
      salesman = User.objects.get(id=val)
      return salesman